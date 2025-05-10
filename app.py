import streamlit as st
import pickle
from funcs import predict_risk_category

with open('model_and_scaler.pkl', 'rb') as f:
    scaler, model = pickle.load(f)

result, conf = '', ''

st.title("Diabetes Risk Assessment Form Using :blue[SVM Machine Learning]")

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
    age_scr = 0 if age < 45 else 2 if age >= 45 and age <= 54 else 3 if age >= 55 and age <= 64 else 4
    bmi_scr = 0 if bmi < 25 else 1 if bmi >= 25 and bmi <= 30 else 3
    m_waist_scr = 0 if gender == 'Female' else 0 if waist < 94 else 3 if waist >= 94 and waist <= 102 else 4
    f_waist_scr = 0 if gender == 'Male' else 0 if waist < 80 else 3 if waist >= 80 and waist <= 88 else 4
    phy_act_scr = 0 if phy_act == 'Yes' else 2
    diet_scr = 0 if diet == 'Every day' else 1
    bp_med_scr = 0 if bp_med == 'No' else 2
    high_glu_scr = 0 if high_glu == 'No' else 5
    fam_mem_scr = 0 if fam_mem == 'No' else 5 if fam_mem == 'Yes: parent, brother, sister, or own child' else 3

    feats = [bmi_scr, phy_act_scr, diet_scr, bp_med_scr, high_glu_scr, fam_mem_scr, m_waist_scr, f_waist_scr, age_scr]
    
    result, conf = predict_risk_category(model, scaler, *feats)

container = st.container(border=True)
container.write("### Predictions")
container.write(f'Risk: {result}')
container.write(f'Confidence: {conf}')