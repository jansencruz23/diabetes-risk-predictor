import streamlit as st
import pickle

with open('model_and_scaler.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

form = st.form('form')
age = form.slider('Age', 0, 120)