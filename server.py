from flask import Flask, request, jsonify
import json
import pandas as pd
import numpy as np

from movie_recommendation import get_recommended_movies

app = Flask(__name__)
df = pd.read_csv("IMDB_movies_big_dataset_clean.csv", low_memory=False, error_bad_lines=False)

def get_movies_by_keyword(keyword):
	movies_by_keyword = pd.DataFrame()
	movies_by_keyword = df[df["original_title"].str.contains(keyword, regex=False)]
	return movies_by_keyword['original_title'].to_json()

@app.route('/')
def index():
    return 'Hello world'

# Preluare titluri filme dupa cuvant cheie
@app.route('/search-movie', methods=['POST'])
def searchMovie():
    data = request.get_json()
    keyword = data["keyword"]
    result = get_movies_by_keyword(keyword)
    return result

@app.route('/recommended-movies', methods=['POST'])
def recommendedMovies():
    data = request.get_json()
    movie = data["movie"]
    result = get_recommended_movies(movie)
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
