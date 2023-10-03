from fastapi import FastAPI
from typing import List, Dict
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = FastAPI()

grouped_genre = pd.read_csv('grouped_genre.csv')
items = pd.read_parquet('items.parquet')
steam_games = pd.read_csv('steam_games.csv')
steam_data = pd.read_csv('steam_data.csv')
games_data = pd.read_csv('games_data.csv')

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de datos de Steam"}

@app.get("/playtime_genre/{genre}")
def PlayTimeGenre(genre: str):
    play_time_genre = grouped_genre[grouped_genre['genres'] == genre] 
    play_time_genre = grouped_genre.sort_values(by='playtime_forever',ascending=False).iloc[0]['year']

    return {"Año con más horas jugadas para Género X": int(play_time_genre)}

@app.get("/user_for_genre/{genre}")
def UserForGenre(genre: str):
    sg_f = steam_games[steam_games['genres'].str.contains(genre, case=False, na=False)]
    steam_data = pd.merge(items, sg_f, left_on='item_id', right_on='id', how='inner')
    steam_data['release_date'] = pd.to_datetime(steam_data['release_date'])
    steam_data['release_year'] = steam_data['release_date'].dt.year
    grouped_user = steam_data.groupby(['user_id', 'release_year'])['playtime_forever'].sum().reset_index()

    max_user = grouped_user.groupby('user_id')['playtime_forever'].sum().idxmax()
    horas_anio = grouped_user[grouped_user['user_id'] == max_user][['release_year', 'playtime_forever']].to_dict('records')

    return {"Usuario con más horas jugadas para Género X": max_user, "Horas jugadas": horas_anio}

@app.get("/users_recommend/{year}")
def UsersRecommend(year: int):
    reviews_filtered = steam_data[steam_data['date'].str.contains(str(year), na=False)]
    reviews_filtered = reviews_filtered[(reviews_filtered['recommend'] == True) & (reviews_filtered['sentiment_analysis'] >= 1)]
    top_games = reviews_filtered['title'].value_counts().head(3)
 
    return [{"Puesto {}".format(i + 1): game} for i, game in enumerate(top_games.index)]

@app.get("/users_not_recommend/{year}")
def UsersNotRecommend(year: int):
    reviews_filtered = steam_data[steam_data['date'].str.contains(str(year), na=False)]
    reviews_filtered = reviews_filtered[(reviews_filtered['recommend'] == False) & (reviews_filtered['sentiment_analysis'] == 0)]

    top_ngames = reviews_filtered['title'].value_counts().head(3)

    return [{"Puesto {}".format(i + 1): game} for i, game in enumerate(top_ngames.index)]

@app.get("/sentiment_analysis/{year}")
def sentiment_analysis(year: int):
    steam_data['release_date'] = pd.to_datetime(steam_data['release_date'])
    review_year = steam_data[steam_data['release_date'].dt.year == year]
    
    negative = (review_year['sentiment_analysis'] == 0).sum()
    neutral = (review_year['sentiment_analysis'] == 1).sum()
    positive = (review_year['sentiment_analysis'] == 2).sum()
    
    return {'Negative': int(negative),'Neutral': int(neutral),'Positive': int(positive)}

@app.get("/recommend_games/{product_id}")
def recomendacion_juego(product_id):

    games_data['combined_features'] = games_data['genres'] + ' ' + games_data['tags']

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(games_data['combined_features'])

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    index = games_data[games_data['item_id'] == product_id].index[0]

    sim_scores = list(enumerate(cosine_sim[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_games_indices = [i[0] for i in sim_scores[1:6]]
    top_games = games_data['item_name'].iloc[top_games_indices]

    return top_games.tolist()

