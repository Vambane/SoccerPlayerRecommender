'''
python file for data preprocessing
'''
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df_sub):
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
    
    df_selected = df_sub[selected_columns]
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df_selected)

    return scaled_df