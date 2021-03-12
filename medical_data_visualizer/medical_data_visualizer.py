import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
medical = pd.read_csv('medical_examination.csv', index_col='id')

# Add 'bmi' and 'overweight' columns
bmi = medical['weight'] / (medical['height'] / 100) ** 2
medical['bmi'] = bmi.round(2)
overweight_true_filter = bmi > 25
overweight_false_filter = bmi <= 25
medical['overweight'] = None
medical.loc[overweight_true_filter, 'overweight'] = 1
medical.loc[overweight_false_filter, 'overweight'] = 0

# Normalize data
# Make 0 always good and 1 always bad.
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0.
# If the value is more than 1, make the value 1.
medical.loc[:, 'cholesterol'] = medical['cholesterol'].map({1: 0, 2: 1, 3: 1})
medical.loc[:, 'gluc'].replace({1: 0, 2: 1, 3: 1}, inplace=True)


# Draw Categorical Plot
def draw_cat_plot():

    # df_cat = None

    # Create DataFrame for cat plot using `pd.melt` using just the values from
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    subjective_features = ['smoke', 'alco', 'active']
    examination_features = ['cholesterol', 'gluc', 'overweight']
    target = 'cardio'
    features = medical.loc[:, subjective_features + examination_features + [target]]

    melted = pd.melt(features, id_vars='cardio')

    fig = plt.figure(figsize=(5, 10))
    ax1 = fig.add_axes([0, 0, 1, 0.5])
    ax0 = fig.add_axes([0, 0.6, 1, 0.5])

    cols = sorted(list(features.drop('cardio', axis=1).columns))

    sns.countplot(x='variable', hue='value', data=melted[melted.cardio == 0],
                  ax=ax0,
                  hue_order=(0, 1),
                  order=cols)
    sns.countplot(x='variable', hue='value', data=melted[melted.cardio == 1],
                  ax=ax1,
                  hue_order=(0, 1),
                  order=cols)

    ax0.set_ylabel('total')
    ax1.set_ylabel('total')
    ax0.set_title('cardio = 0')
    ax1.set_title('cardio = 1')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    # df_cat = None
    # Draw the catplot with 'sns.catplot()'

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# # Draw Heat Map
# def draw_heat_map():
#     # Clean the data
#     df_heat = None
#
#     # Calculate the correlation matrix
#     corr = None
#
#     # Generate a mask for the upper triangle
#     mask = None
#
#
#
#     # Set up the matplotlib figure
#     fig, ax = None
#
#     # Draw the heatmap with 'sns.heatmap()'
#
#
#
#     # Do not modify the next two lines
#     fig.savefig('heatmap.png')
#     return fig
