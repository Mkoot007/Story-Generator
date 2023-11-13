import streamlit as st
from transformers import pipeline, set_seed
import tensorflow as tf 
# import torch as pytorch


text_generator = pipeline("text2text-generation", model="google/flan-t5-base")

st.title("Story Generator")

title = st.text_input("Title of the Story:")
character = st.text_input("Character (Hero) Name:")
era = st.selectbox("Era of the Story:", ["Medieval", "Modern", "Future"])
genre = st.selectbox("Genre:", ["Action", "Novelistic", "Love"])
punchline = st.text_area("Punchline (Describe what the story is about):")
story_length = st.slider("Story Length", min_value=100, max_value=2000, step=100)
generate_button = st.button("Generate Story")

if generate_button:
    if title and character and punchline:
        prompt = f"Write a {genre} story titled '{title}' set in the {era} era. The main character, {character}, faces a {genre} adventure. The story is about '{punchline}'."

        set_seed(42)
        full_story = text_generator(prompt, max_length=story_length, do_sample=True)[0]["generated_text"]

        st.markdown(full_story)
    else:
        st.warning("Please provide a title, character name, and punchline.")
