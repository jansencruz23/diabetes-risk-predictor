import streamlit as st
import pickle

with open('model_and_scaler.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

form = st.form('form')
age = form.number_input('Age', step=1, min_value=0, max_value=120)
bmi = form.number_input('BMI', min_value=0.0, max_value=200.0)
gender = form.radio(
    'Gender',
    ['Male', 'Female']
)
waist = form.number_input('Waist in cm', step=0.25, min_value=0.0)

phy_act = form.radio(
    'Do you usually have daily at least 30 minutes of physical activity at work and/or during leisure time (including normal daily activity)?',
    ['Yes', 'No']
)
diet = form.radio(
    'How often do you eat vegetables, fruit, or berries?',
    ['Every day', 'Not every day']
)
bp_med = form.radio(
    'Have you ever taken medication for high blood pressure on regular basis?',
    ['Yes', 'No']
)
high_glu = form.radio(
    'Have you ever been found to have high blood glucose (e.g. in a health examination, during an illness, during pregnancy)?',
    ['Yes', 'No']
)
fam_mem = form.radio(
    'Have any of the members of your immediate family or other relatives been diagnosed with diabetes (type 1 or type 2)?',
    ['Yes: grandparents, aunt, uncle or first cousin (but no own parent, brother, sister, or child)', 'Yes: parent, brother, sister, or own child', 'No']
)
submit = form.form_submit_button('Submit')

if submit:
    print(type(age))
    