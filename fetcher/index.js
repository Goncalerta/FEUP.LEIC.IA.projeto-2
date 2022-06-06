const express = require('express');
const app = express();
require('dotenv').config();

const SpotifyWebApi = require('spotify-web-api-node');

var spotifyApi = new SpotifyWebApi({
  clientId: process.env.CLIENT_ID,
  clientSecret: process.env.CLIENT_SECRET
});

spotifyApi.clientCredentialsGrant().then(
  function (data) {
    console.log("The access token expires in " + data.body["expires_in"]);
    console.log("The access token is " + data.body["access_token"]);

    // Save the access token so that it's used in future calls
    spotifyApi.setAccessToken(data.body["access_token"]);
  },
  function (err) {
    console.log("Something went wrong when retrieving an access token", err);
  }
);

app.get('/getGenres', function(req, res) {
  spotifyApi.getAvailableGenreSeeds()
      .then(function(data) {
        const genreSeeds = data.body;
        res.send(genreSeeds);
      }, function(err) {
        console.log('Something went wrong!', err);
      });
});

app.get('/getMusicsOfGenre/:genre', function(req, res) {
  const genre = req.params.genre; 
  spotifyApi.getRecommendations({
    seed_genres: [genre],
    limit: 100,
    })
  .then(function(data) {
    let recommendations = data.body;
    let tracks = [];
    for (let track of recommendations.tracks) {
        const {external_urls, id, name, explicit, artists, popularity} = track;
        const {id: artistId, name: artist} = artists[0];
        const {release_date: date, release_date_precision: precision_date} = track.album;
        tracks.push({external_urls, id, name, explicit, artistId, artist, popularity, date, precision_date});
      }
    res.send(tracks);
  }, function(err) {
    console.log("Something went wrong!", err);
  });
});

app.get('/getArtistGenres/:artist', function(req, res) {
  const artist = req.params.artist; 
  spotifyApi.getArtist(artist)
    .then(function(data) {
      const {genres} = data.body;
      res.send(genres);
    }, function(err) {
      console.error(err);
    });
});

app.get('/getTrackFeatures/:trackID', function(req, res) {
  const trackID = req.params.trackID;
  spotifyApi.getAudioFeaturesForTrack(trackID)
  .then(function(data) {
    let trackFeatures = data.body;
    res.send(trackFeatures);
  }, function(err) {
    console.log("Something went wrong!", err);
  });
});

const server = app.listen(8005, function() {
  const host = server.address().address;
  const port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
