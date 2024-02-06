'''
the cosine similarity is computed in this py script
'''
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(scaled_df):
    similarity_matrix = cosine_similarity(scaled_df)
    return similarity_matrix