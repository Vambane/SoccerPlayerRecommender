import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# loading the data
df = pd.read_csv('https://raw.githubusercontent.com/Vambane/SoccerPlayerRecommender/main/FullData.csv')
df_sub = pd.read_csv('https://raw.githubusercontent.com/Vambane/SoccerPlayerRecommender/main/df_sub.csv')

# selecting the relevant columns for similarity calculation
selected_columns = ['Rating', 'Age', 'Height', 'Weight', 'Weak_foot', 'Skill_Moves', 'Ball_Control',
                    'Dribbling', 'Marking', 'Sliding_Tackle', 'Standing_Tackle', 'Aggression',
                    'Reactions', 'Attacking_Position', 'Interceptions', 'Vision', 'Composure',
                    'Crossing', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength',
                    'Balance', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
                    'Long_Shots', 'Curve', 'Freekick_Accuracy', 'Penalties', 'Volleys',
                    'GK_Positioning', 'GK_Diving', 'GK_Kicking', 'GK_Handling', 'GK_Reflexes', 'cm',
                    'rb', 'st', 'gk', 'lw', 'rw', 'lb', 'cdm', 'lwb', 'cam', 'rm', 'lm',
                    'cf', 'cb', 'rwb', 'low', 'medium', 'high ', 'low ', 'high', 'medium ',
                    'Cluster', 'PC1', 'PC2', 'Component 1', 'Component 2'
                    ]

# creating a subset using the selected columns above
df_selected = df_sub[selected_columns]

# calculate cosine similarity matrix
similarity_matrix = cosine_similarity(df_selected)

# function to get player recommendations
def get_player_recommendations(player_name, age_filter=None, num_recommendation=10):
    player_index = df_sub[df_sub['Name'] == player_name].index[0]
    similar_players = list(enumerate(similarity_matrix[player_index]))
    similar_players = sorted(similar_players, key=lambda x: x[1], reverse=True)

    # exclude the player, we are searching
    similar_players = similar_players[1: num_recommendation + 1]

    # filtering out players that have sub or res as their position
    similar_players = [(index, similarity) for index, similarity in similar_players
                       if abs(df.iloc[index]['Club_Position'] not in ['Sub', 'Res'])]
    
    if age_filter is not None:
        similar_players = [(index, similarity) for index, similarity in similar_players
                           if abs(df_selected.iloc[index]['Age'] - age_filter) <= 5]
        
    recommended_players = [(df.iloc[index]['Name'], df.iloc[index]['Age'],
                            df.iloc[index]['Rating'], df.iloc[index]['Club_Position'])
                            for index, _ in similar_players]
    
    return recommended_players

# Streamlit app
st.title('Player Recommendation App')

# Sidebar with user input
player_name = st.sidebar.text_input('Enter player name:')
age_filter = st.sidebar.slider('Age Filter', 15, 45, 30)
num_recommendations = st.sidebar.slider('Number of recommendations', 1, 20, 10)

# Display recommendations
if st.sidebar.button('Get Recommendation'):
    recommended_players = get_player_recommendations(player_name, age_filter, num_recommendations)
    st.write(f"Recommender players for {player_name} (Age Filter: {age_filter}): ")
    for i, (name, age, rating, position) in enumerate(recommended_players, start=1):
        st.write(f"{i}, {name} (Age: {age}, Rating: {rating}, Position: {position})")# loading the data
df = pd.read_csv('https://raw.githubusercontent.com/Vambane/SoccerPlayerRecommender/main/FullData.csv')
df_sub = pd.read_csv('https://raw.githubusercontent.com/Vambane/SoccerPlayerRecommender/main/df_sub.csv')

# selecting the relevant columns for similarity calculation
selected_columns = ['Rating', 'Age', 'Height', 'Weight', 'Weak_foot', 'Skill_Moves', 'Ball_Control',
                    'Dribbling', 'Marking', 'Sliding_Tackle', 'Standing_Tackle', 'Aggression',
                    'Reactions', 'Attacking_Position', 'Interceptions', 'Vision', 'Composure',
                    'Crossing', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Stamina', 'Strength',
                    'Balance', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
                    'Long_Shots', 'Curve', 'Freekick_Accuracy', 'Penalties', 'Volleys',
                    'GK_Positioning', 'GK_Diving', 'GK_Kicking', 'GK_Handling', 'GK_Reflexes', 'cm',
                    'rb', 'st', 'gk', 'lw', 'rw', 'lb', 'cdm', 'lwb', 'cam', 'rm', 'lm',
                    'cf', 'cb', 'rwb', 'low', 'medium', 'high ', 'low ', 'high', 'medium ',
                    'Cluster', 'PC1', 'PC2', 'Component 1', 'Component 2'
                    ]

# creating a subset using the selected columns above
df_selected = df_sub[selected_columns]

# Scaling the data
scaler = StandardScaler() #Instantiate the standard scaler
scaled_df = scaler.fit_transform(df_selected)

# calculate cosine similarity matrix
similarity_matrix = cosine_similarity(df_selected)

# function to get player recommendations
def get_player_recommendations(player_name, age_filter=None, num_recommendation=10):
    player_index = df_sub[df_sub['Name'] == player_name].index[0]
    similar_players = list(enumerate(similarity_matrix[player_index]))
    similar_players = sorted(similar_players, key=lambda x: x[1], reverse=True)

    # exclude the player, we are searching
    similar_players = similar_players[1: num_recommendation + 1]

    # filtering out players that have sub or res as their position
    similar_players = [(index, similarity) for index, similarity in similar_players
                       if abs(df.iloc[index]['Club_Position'] not in ['Sub', 'Res'])]
    
    if age_filter is not None:
        similar_players = [(index, similarity) for index, similarity in similar_players
                           if abs(df_selected.iloc[index]['Age'] - age_filter) <= 5]
        
    recommended_players = [(df.iloc[index]['Name'], df.iloc[index]['Age'],
                            df.iloc[index]['Rating'], df.iloc[index]['Club_Position'])
                            for index, _ in similar_players]
    
    return recommended_players

# Streamlit app
st.title('Player Recommendation App')

# Sidebar with user input
player_name = st.sidebar.text_input('Enter player name:')
age_filter = st.sidebar.slider('Age Filter', 15, 45, 30)
num_recommendations = st.sidebar.slider('Number of recommendations', 1, 20, 10)

# Display recommendations
if st.sidebar.button('Get Recommendation'):
    recommended_players = get_player_recommendations(player_name, age_filter, num_recommendations)
    st.write(f"Recommender players for {player_name} (Age Filter: {age_filter}): ")
    for i, (name, age, rating, position) in enumerate(recommended_players, start=1):
        st.write(f"{i}, {name} (Age: {age}, Rating: {rating}, Position: {position})")