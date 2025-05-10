classes = ['high', 'low', 'moderate', 'slightly elevated', 'very high']

def predict_risk_category(svm_model, scaler, 
    BMI_Score, Phys_Active, Diet_Score, BP_Meds, Blood_Glucose, Family_History, Waist_Male, Waist_Female, Age
):

    input_data = [[
        int(BMI_Score),
        int(Phys_Active),
        int(Diet_Score),
        int(BP_Meds),
        int(Blood_Glucose),
        int(Family_History),
        int(Waist_Male),
        int(Waist_Female),
        int(Age)
    ]]

    input = scaler.transform(input_data)
    prediction = svm_model.predict(input)[0]
    probabilities  = svm_model.predict_proba(input)
    conf = f'{(probabilities[:, classes.index(prediction)] * 100)[0]:.2f}%'

    return prediction, conf