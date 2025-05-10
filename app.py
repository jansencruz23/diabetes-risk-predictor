import streamlit as st
import pickle
from funcs import predict_risk_category

risk_colors = {
    'low': '<span style="color:green;">Low</span>',
    'slightly elevated': '<span style="color:goldenrod;">Slightly Elevated</span>',
    'moderate': '<span style="color:orange;">Moderate</span>',
    'high': '<span style="color:deeppink;">High</span>',
    'very high': '<span style="color:red;">Very High</span>'
}


# load model and scaler
with open('model_and_scaler.pkl', 'rb') as f:
    scaler, model = pickle.load(f)

# page title
st.title("Diabetes Risk Assessment Form Using :blue[SVM Machine Learning]")

# forms
with st.form('risk_form'):
    age = st.number_input('Age', step=1, min_value=0, max_value=120)
    bmi = st.number_input('BMI', min_value=0.0, max_value=200.0)
    gender = st.radio('Gender', ['Male', 'Female'])
    waist = st.number_input('Waist in cm', step=0.25, min_value=0.0)

    phy_act = st.radio(
        'Do you have at least 30 minutes of daily physical activity?',
        ['Yes', 'No']
    )
    diet = st.radio(
        'How often do you eat vegetables, fruit, or berries?',
        ['Every day', 'Not every day']
    )
    bp_med = st.radio(
        'Have you taken medication for high blood pressure regularly?',
        ['Yes', 'No']
    )
    high_glu = st.radio(
        'Have you ever had high blood glucose?',
        ['Yes', 'No']
    )
    fam_mem = st.radio(
        'Family history of diabetes?',
        [
            'Yes: grandparents, aunt, uncle or first cousin',
            'Yes: parent, sibling, or child',
            'No'
        ]
    )

    submitted = st.form_submit_button('Submit')

# after submission
if submitted:
    age_scr = 0 if age < 45 else 2 if age >= 45 and age <= 54 else 3 if age >= 55 and age <= 64 else 4
    bmi_scr = 0 if bmi < 25 else 1 if bmi >= 25 and bmi <= 30 else 3
    m_waist_scr = 0 if gender == 'Female' else 0 if waist < 94 else 3 if waist >= 94 and waist <= 102 else 4
    f_waist_scr = 0 if gender == 'Male' else 0 if waist < 80 else 3 if waist >= 80 and waist <= 88 else 4
    phy_act_scr = 0 if phy_act == 'Yes' else 2
    diet_scr = 0 if diet == 'Every day' else 1
    bp_med_scr = 0 if bp_med == 'No' else 2
    high_glu_scr = 0 if high_glu == 'No' else 5
    fam_mem_scr = 0 if fam_mem == 'No' else 5 if fam_mem == 'Yes: parent, brother, sister, or own child' else 3

    features = [
        bmi_scr, phy_act_scr, diet_scr, bp_med_scr,
        high_glu_scr, fam_mem_scr, m_waist_scr, f_waist_scr, age_scr
    ]
    
    risk, conf = predict_risk_category(model, scaler, *features)
    risk_formatted = risk_colors.get(risk.lower(), risk)

    with st.container(border=True):
        st.write("### Predictions")
        st.markdown(f"**Risk:** {risk_formatted}", unsafe_allow_html=True)
        st.write(f"**Confidence:** {conf}")