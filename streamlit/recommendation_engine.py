import pandas as pd

def get_player_recommendations(df, df_sub, similarity_matrix, player_name, age_filter=None, num_recommendation=10):
    player_index = df_sub[df_sub['Name'] == player_name].index[0]
    similar_players = list(enumerate(similarity_matrix[player_index]))
    similar_players = sorted(similar_players, key=lambda x: x[1], reverse=True)

    similar_players = similar_players[1: num_recommendation + 1]
    similar_players = [(index, similarity) for index, similarity in similar_players
                       if abs(df.iloc[index]['Club_Position'] not in ['Sub', 'Res'])]

    if age_filter is not None:
        similar_players = [(index, similarity) for index, similarity in similar_players
                           if abs(df_sub.iloc[index]['Age'] - age_filter) <= 5]

    recommended_players = [(df.iloc[index]['Name'], df.iloc[index]['Age'],
                            df.iloc[index]['Rating'], df.iloc[index]['Club_Position'])
                           for index, _ in similar_players]

    return recommended_players