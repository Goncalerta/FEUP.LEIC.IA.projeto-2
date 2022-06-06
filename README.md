# Spotify Top Hits (2000-2019): Predicting a song's genre

This project was done by the group 09_1B of the Artificial Intelligence course unit at FEUP in 2022:
    - João Ferreira Baltazar - up201905616@edu.fe.up.pt
    - Nuno Teixeira Costa - up201906272@edu.fe.up.pt
    - Pedro Gonçalo Correia - up201905348@edu.fe.up.pt

## Usage

This project was made with `Python 3.9.9` and requires Jupyter notebooks and the following libraries:
    - pandas 1.4.1
    - seaborn 0.11.2
    - IPython 8.0.1
    - matplotlib 3.5.1
    - numpy 1.19.5
    - sklearn 1.0.2

To run the code, open the Jupyter Notebook `project.ipynb` and run the desired cells, provided you are using Python 3.9.9 and the aforementioned libraries.

## Spotify API Fetcher

To complement the project with a better dataset, we implemented a program that calls the Spotify API and generates a dataset of songs. This can be found in the folder `fetcher`.

For the fetcher, Node is required as well as Python 3.9.9. To run it, you should:

    - enter the fetcher folder
    - run the node server
    - execute the python script on a different shell in the same folder

The .csv file will be placed in the fetcher folder when finished.
