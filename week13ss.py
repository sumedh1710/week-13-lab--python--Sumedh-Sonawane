import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sampled_dataset = pd.read_csv('C:\Dell\Desktop\python final project dataset\sampled_dataset.csv')

st.set_option('deprecation.showPyplotGlobalUse', False)

# Scatter plot function
def scatter_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='danceability', y='popularity', data=sampled_dataset, hue='energy', size='tempo', sizes=(20, 200))
    plt.title('Popularity vs Danceability with Energy and Tempo')
    plt.xlabel('Danceability')
    plt.ylabel('Popularity')
    plt.legend(title='Energy')
    st.pyplot(fig)

subset = st.checkbox('Show Subset of Data', False)
if subset:
    st.dataframe(sampled_dataset.head(10))  


scatter_plot()
