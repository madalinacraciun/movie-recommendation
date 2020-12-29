from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

def get_movies_by_keyword(keyword):
	df = pd.read_csv("IMDB_movies_big_dataset_clean.csv", low_memory=False, error_bad_lines=False)
	movies_by_keyword = pd.DataFrame()
	movies_by_keyword = df[df["original_title"].str.contains(keyword, regex=False)]
	return movies_by_keyword['original_title'].to_json()

@app.route('/')
def index():
    return 'Hello world'

@app.route('/search-movie', methods=['POST'])
def searchMovie():
    data = request.get_json()
    keyword = data["movie"]
    result = get_movies_by_keyword(keyword)
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
