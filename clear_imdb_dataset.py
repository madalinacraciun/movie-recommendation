import pandas as pd
import array
df = pd.read_csv("IMDB_movies_dataset.csv", low_memory=False, error_bad_lines=False)
df['language'] = df['language'].fillna('')

filtered_csv = pd.DataFrame()
for i in range(1960, 2020):
    temp = df[df['year'] == str(i)]
    filtered_csv = pd.concat([filtered_csv, temp], axis=0)

filtered_csv = filtered_csv[filtered_csv['language'].str.contains('English', regex=False)]

filtered_csv = filtered_csv[filtered_csv['avg_vote'].astype(float)>=6]

arr = []
for j in range(0,filtered_csv.shape[0]):
    arr.append(j)

filtered_csv["id"] = arr
    
filtered_csv.to_csv('IMDB_movies_big_dataset_clean.csv')