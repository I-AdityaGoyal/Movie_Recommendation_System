import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=a6437a77b13974020f3220f6f9c30e6f&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    movie_index = movies[movies["title"]==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similar.pkl','rb'))
st.title('Movie Recommender System')
st.markdown('By Aditya Goyal')

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values 
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.text(names[i])
        col.image(posters[i])
