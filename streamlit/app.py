# app.py
import streamlit as st
import pandas as pd
from data_preprocessing import preprocess_data
from similarity_calculator import calculate_similarity
from recommendation_engine import get_player_recommendations

# loading the data
df = pd.read_csv('https://raw.githubusercontent.com/Vambane/SoccerPlayerRecommender/main/FullData.csv')
df_sub = pd.read_csv('https://raw.githubusercontent.com/Vambane/SoccerPlayerRecommender/main/df_sub.csv')

# preprocessing the data
scaled_df = preprocess_data(df_sub)

# calculating similarity
similarity_matrix = calculate_similarity(scaled_df)

# Streamlit app
st.title('Player Recommendation App')

# Sidebar with user input
column_name = 'Name'
player_name = st.selectbox('Enter player name:', options=df[column_name].unique())

age_filter = st.sidebar.slider('Age Filter', 15, 45, 30)
num_recommendations = st.sidebar.slider('Number of recommendations', 1, 20, 10)

# Display recommendations
if st.sidebar.button('Get Recommendation'):
    recommended_players = get_player_recommendations(df, df_sub, similarity_matrix, player_name, age_filter, num_recommendations)
    st.write(f"Recommender players for {player_name} (Age Filter: {age_filter}): ")
    for i, (name, age, rating, position) in enumerate(recommended_players, start=1):
        st.write(f"{i}, {name} (Age: {age}, Rating: {rating}, Position: {position})")
