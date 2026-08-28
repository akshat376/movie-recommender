# Movie Recommender

## Problem

Recommend movies similar to a user's selected movie using a content-based recommendation system.

## Dataset

TMDB movie dataset containing movie information used to determine similarity between movies.

## Key Findings

* Content-based filtering can recommend movies based on similarity to a selected title
* Cosine similarity is used to identify movies with similar content
* The system returns the top 5 most similar movies for a given title
* Movie title matching is case-insensitive for easier user input

## Approach

* Loaded and processed movie data from the TMDB dataset
* Used content-based filtering to calculate movie similarities
* Applied cosine similarity to identify similar movies
* Stored precomputed recommendation indices using Joblib
* Built an interactive Streamlit interface for entering movie titles and viewing recommendations
* Added handling for empty inputs and movies not present in the dataset

## Result

A Streamlit-based movie recommendation app that takes a movie title as input and returns 5 similar movie recommendations.

## Files

* `app.py` — Streamlit application containing the recommendation logic and user interface
* `movies.pkl` — Serialized movie dataset
* `sorted_indices.pkl` — Precomputed sorted similarity indices used for recommendations
* `requirements.txt` — Python dependencies required to run the application
