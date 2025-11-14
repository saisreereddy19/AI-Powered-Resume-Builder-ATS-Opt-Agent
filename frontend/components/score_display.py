import streamlit as st

def show_scores(scores):
    st.metric("Semantic Score", scores["semantic_score"])
    st.metric("Keyword Score", scores["keyword_score"])
    st.metric("Final Score", scores["final_score"])
