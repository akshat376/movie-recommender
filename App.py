import streamlit as st
import joblib
import pandas as pd

# Load saved data
similarity_matrix = joblib.load('sorted_indices.pkl')
movies = joblib.load('movies.pkl')

# Page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.title("🎬 Movie Recommender")
st.markdown("Type a movie you like and get 5 similar recommendations.")

# Input
movie_input = st.text_input("Enter a movie title", placeholder="e.g. The Dark Knight")

# Recommend button
if st.button("Recommend"):
    if movie_input.strip() == "":
        st.warning("Please enter a movie title.")
    else:
        # Check if movie exists (case-insensitive)
        match = movies[movies['title'].str.lower() == movie_input.lower()]
        
        if match.empty:
            st.error(f"'{movie_input}' not found in dataset. Try another title.")
        else:
            # Get index and similarity scores
            movie_index = match.index[0]
            indices = similarity_matrix[movie_index][:5]
            recommendations = movies['title'].iloc[indices].tolist()

            # Display results
            st.subheader(f"Because you liked **{movie_input}**:")
            for i, title in enumerate(recommendations, 1):
                st.markdown(f"**{i}.** {title}")