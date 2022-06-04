import requests
import pandas as pd
from datetime import datetime

baseURL = "http://localhost:8081/"

genres = [
    "acoustic",
    "afrobeat",
    "alt-rock",
    "alternative",
    "ambient",
    "black-metal",
    "bluegrass",
    "blues",
    "bossanova",
    "breakbeat",
    "cantopop",
    "classical",
    "comedy",
    "country",
    "dancehall",
    "death-metal",
    "deep-house",
    "disco",
    "drum-and-bass",
    "dub",
    "dubstep",
    "edm",
    "electronic",
    "emo",
    "folk",
    "forro",
    "funk",
    "garage",
    "gospel",
    "goth",
    "grindcore",
    "groove",
    "grunge",
    "hard-rock",
    "hardcore",
    "hardstyle",
    "heavy-metal",
    "hip-hop",
    "house",
    "idm",
    "indie",
    "indie-pop",
    "industrial",
    "jazz",
    "latino",
    "metal",
    "metalcore",
    "minimal-techno",
    "mpb",
    "new-age",
    "opera",
    "pop",
    "psych-rock",
    "punk",
    "punk-rock",
    "r-n-b",
    "reggae",
    "reggaeton",
    "rock",
    "rock-n-roll",
    "rockabilly",
    "salsa",
    "samba",
    "sertanejo",
    "ska",
    "soul",
    "synth-pop",
    "tango",
    "techno",
    "trance",
    "trip-hop",
]


def getTrackGenres(track, origGenre):
    artistGenres = requests.get(
        baseURL + f'getArtistGenres/{track["artistId"]}').json()

    trackGenres = []

    for genre in artistGenres:
        strippedGenre = genre.replace("cover", "")
        if strippedGenre in genres:
            trackGenres.append(strippedGenre)

    if trackGenres == []:
        trackGenres = [origGenre]

    return " ".join(list(set(trackGenres)))


def getYear(date, precision):
    if (precision == "day"):
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return str(date_obj.year)
    if (precision == "year"):
        return date
    else:
        print(f'Invalid precision: {precision} {date}')
        return ''


fetchedTracks = []

for genre in genres[0:1]:
    tracks = requests.get(baseURL + f'getMusicsOfGenre/{genre}').json()
    for track in tracks:
        trackGenres = getTrackGenres(track, genre)
        features = requests.get(
            baseURL + f'getTrackFeatures/{track["id"]}').json()
        fetchedTracks.append({
            "artist": track["artist"],
            "song": track["name"],
            "duration_ms": features["duration_ms"],
            "explicit": track["explicit"],
            "year": getYear(track["date"], track["precision_date"]),
            "popularity": track["popularity"],
            "danceability": features["danceability"],
            "energy": features["energy"],
            "key": features["key"],
            "loudness": features["loudness"],
            "mode": features["mode"],
            "speechiness": features["speechiness"],
            "acousticness": features["acousticness"],
            "instrumentalness": features["instrumentalness"],
            "liveness": features["liveness"],
            "valence": features["valence"],
            "tempo": features["tempo"],
            "genre": trackGenres
        })


df = pd.DataFrame(fetchedTracks)
df.to_csv('tracks.csv', index=False)
