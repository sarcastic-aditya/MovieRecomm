import streamlit as st
import pickle 
import pandas as pd
import requests
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_dict)
st.title('Movie Recommendation')
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Select an option', movies['title'].values)
st.write('You selected:', selected_option)
def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=44ebbb14aa5c4a28107187eca305cfe2&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movie=[]
    recommend_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recommend_movie_poster.append(poster(movie_id))
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie,recommend_movie_poster
if st.button('Recommend'):
    name,posterss=recommend(selected_option)
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
        st.text(name[0])
        st.image(posterss[0])
    with c2:
        st.text(name[1])
        st.image(posterss[1])
    with c3:
        st.text(name[2])
        st.image(posterss[2])
    with c4:
        st.text(name[3])
        st.image(posterss[3])
    with c5:
        st.text(name[4])
        st.image(posterss[4])