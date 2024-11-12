import pickle
import streamlit as st
import pandas as pd




# Load Hollywood movies and similarity data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Load Bollywood movies and similarity data
movies_dict2 = pickle.load(open('bollywood_movies_dict.pkl', 'rb'))
df = pd.DataFrame(movies_dict2)
similarity2 = pickle.load(open('similarity2.pkl', 'rb'))

# Hollywood recommendation function
def recommend_hollywood(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies 

# Bollywood recommendation function
def recommend_bollywood(movie):
    movie_index2 = df[df['title'] == movie].index[0]
    distance2 = similarity2[movie_index2]
    movies_list2 = sorted(list(enumerate(distance2)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies2 = []
    for i in movies_list2:
        recommended_movies2.append(df.iloc[i[0]].title)
    return recommended_movies2



st.markdown("""
    <style>
    /* Set page background color */
    body {
        background-color: #a4bff5; /* Light sky blue */
        font-family: 'Arial', sans-serif;
    }

    /* Full page background and container */
    .stApp {
        background-color: #a4bff5;
        padding: 20px;
        max-width: 900px;
        margin: 0 auto;
    }

    /* Title styling */
    h1 {
        color: #a10517;
        text-align: center;
        font-size: 40px;
        margin-bottom: 20px;
    }

    /* Recommendation section title */
    .recommendation-title {
        color: #222;
        font-size: 24px;
        margin-top: 20px;
        margin-bottom: 10px;
        text-align: center;
    }

    /* Movie list styling */
    .movie-list {
        background-color: #2972ba;
        border: 1px solid #ddd;
        padding: 10px;
        margin: 10px 0;
        font-size: 16px;
        
    }

    .movie-list:hover {
        background-color: #58b825;
    }

    /* Green buttons with hover effect */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        margin-top: 20px;
        width: 30%;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }

   

    

    /* Footer style */
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #222;
        font-size: 14px;
    }


    </style>
    """, unsafe_allow_html=True)


# Streamlit UI

# Hollywood section
st.markdown("<h1>Hollywood Movie Recommendation System</h1>", unsafe_allow_html=True)
selected_movie_name = st.selectbox('Select a Hollywood movie to get recommendations', movies['title'].values)

if st.button('Recommend Hollywood'):
    st.markdown("<h2 class='recommendation-title'>Recommended Hollywood Movies:</h2>", unsafe_allow_html=True)
    recommendation = recommend_hollywood(selected_movie_name)
    for i in recommendation:
        st.markdown(f"<div class='movie-list'>{i}</div>", unsafe_allow_html=True)

# Bollywood section
st.markdown("<h1>Bollywood Movie Recommendation System</h1>", unsafe_allow_html=True)
selected_movie_name2 = st.selectbox('Select a Bollywood movie to get recommendations', df['title'].values)

if st.button('Recommend Bollywood'):
    st.markdown("<h2 class='recommendation-title'>Recommended Bollywood Movies:</h2>", unsafe_allow_html=True)
    recommendation2 = recommend_bollywood(selected_movie_name2)
    for i in recommendation2:
        st.markdown(f"<div class='movie-list'>{i}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Movie Recommendation System © 2024</div>", unsafe_allow_html=True)