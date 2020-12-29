import pandas as pd
import numpy as np
import json
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("IMDB_movies_big_dataset_clean.csv", low_memory=False, error_bad_lines=False)

def get_title_from_id(id):
	return df[df.id == id]["original_title"].values[0]

def get_year_from_id(id):
	return df[df.id == id]["year"].values[0]

def get_genre_from_id(id):
	return df[df.id == id]["genre"].values[0]

def get_director_from_id(id):
	return df[df.id == id]["director"].values[0]

def get_actors_from_id(id):
	return df[df.id == id]["actors"].values[0]

def get_id_from_title(title):
	return df[df.original_title == title]["id"].values[0]

def get_rating_from_id(id):
	return df[df.id == id]["avg_vote"].values[0]

def get_recommended_movies(movie):
	features = ['original_title','description','actors','genre','director']
	for feature in features:
		df[feature] = df[feature].fillna('')
	df["combined_features"] = df.apply(combine_features,axis=1)
	cv = CountVectorizer()
	count_matrix = cv.fit_transform(df["combined_features"])
	cosine_sim = cosine_similarity(count_matrix)
	movie_index = get_id_from_title(movie)
	similar_movies =  list(enumerate(cosine_sim[movie_index]))
	sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

	final_list = []
	i = 0
	for element in sorted_similar_movies:
		if i>0:
			list_element = {
				'title' : str(get_title_from_id(element[0])),
				'year' : str(get_year_from_id(element[0])),
				'genre' : get_genre_from_id(element[0]),
				'director' : get_director_from_id(element[0]),
				'actors' : get_actors_from_id(element[0])
			}
			final_list.append(list_element)
		i=i+1
		if i>20:
			break
	
	return json.dumps(final_list)


# # Se citeste fisierul CSV ce contine datele despre filme
# print("Introduceti titlul filmului si apasati ENTER: ")
# movie_user_likes = str(input())

# start_time = time.time()

# t1 = time.time()
# df = pd.read_csv("IMDB_movies_big_dataset_clean.csv", low_memory=False, error_bad_lines=False)
# print("Fisierul CSV a fost citit ... (%.2f secunde)" % (time.time()-t1))


# # Se selecteaza caracteristicile ce vor fi luate in seama pentru a calcula scorul de similaritate
# t2 = time.time()
# features = ['original_title','description','actors','genre','director']

# for feature in features:
# 	df[feature] = df[feature].fillna('')

# # Se creeaza o coloana in obiectul DF ce va contine caracteristicile importante pentru scorul de similaritate

def combine_features(row):
	try:
		return row["original_title"] + " " + row["description"] + " " + row['actors'] +" " + row['genre'] + " " + row["director"]
	except:
		print("Error in combining features at :", row)

# df["combined_features"] = df.apply(combine_features,axis=1)
# print("S-a creat coloana ce contine caracteristicile pentru recomandare ...(%.2f secunde)" % (time.time()-t2))


# # Se creeaza matricea de frecvente pentru filme, luand in considerare caracteristicile extrase
# # Matrice ce contine pe linii filmele si pe coloane cuvintele unice de pe coloana "combined_features"
# t3 = time.time()
# cv = CountVectorizer()

# count_matrix = cv.fit_transform(df["combined_features"])
# # print(count_matrix.toarray().shape[0])
# # print(count_matrix.toarray().shape[1])
# print("S-a creat matricea de frecvente ...(%.2f secunde)" % (time.time()-t3))

# # Se calculeaza cosine similarity in functie de matricea de frecvente
# # Matrice patratica 16313 x 16313 ( = numarul de filme din fisierul CSV )
# t4 = time.time()
# cosine_sim = cosine_similarity(count_matrix) 
# print(cosine_sim.shape)
# print("S-a efectuat cosine similarity pe matricea de frecvente ... (%.2f secunde)" % (time.time()-t4))

# # movie_user_likes = "The Avengers"
# # movie_user_likes = "Titanic"
# # movie_user_likes = "John Wick"

# # Se preia id-ul filmului din titlul oferit de catre utilizator
# movie_index = get_id_from_title(movie_user_likes)

# # Se preia randul din matricea de similaritate ce contine filmul oferit de utilizator si se creeaza o enumeratie de tipul
# # (id_film, scor de silimaritate) cu care se construieste lista de filme similare
# similar_movies =  list(enumerate(cosine_sim[movie_index]))

# # Se preia o lista cu filme similare, sortata in ordine descrescatoare dupa scorul de similaritate
# # x[0] = id-ul filmului
# # x[1] = scorul de similaritate al filmului din enumeratie
# sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

# # sorted_by_rating = sorted_similar_movies[0:14]


# # Se afiseaza in consola primele 30 de filme similare cu filmul introdus de utilizator
# i=0
# print("Top 30 filme similare cu "+movie_user_likes+" sunt :\n")
# for element in sorted_similar_movies:
# 	# Se extrage element[0] din enumeratie, ce reprezinta id-ul unui film din setul de date si se extrage apoi titlul filmului cu acest id
# 		print(get_title_from_id(element[0]))
# 		i=i+1
# 		if i>30:
# 			break

# total_time = time.time() - start_time
# print("--- Timpul total de executie al algoritmului : %.2f secunde ---" % (total_time))