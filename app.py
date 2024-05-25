import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/colab_files_to_train_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/colab_files_to_train_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/colab_files_to_train_models/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(f'{working_dir}/colab_files_to_train_models/breast_cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart','person','lungs'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':

    # page title
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        rm = st.text_input('Radius_mean')

    with col2:
        tm = st.text_input('Texture_mean')

    with col3:
        pm = st.text_input('Perimeter_mean')

    with col4:
        am = st.text_input('Area_mean')

    with col5:
        sm = st.text_input('Smoothness_mean')
    
    with col6:
        cm = st.text_input('Compactness_mean')

    with col1:
        Cm = st.text_input('Concavity_mean')

    with col2:
        cpm = st.text_input('Con_points_mean')

    with col3:
        Sm = st.text_input('Symmetry_mean')

    with col4:
        fdm = st.text_input('Fractal_D_mean')

    with col5:
        rs = st.text_input('Radius_se')
    
    with col6:
        ts = st.text_input('Texture_se')

    with col1:
        ps = st.text_input('Perimeter_se')

    with col2:
        As = st.text_input('Area_se')

    with col3:
        ss = st.text_input('Smoothness_se')

    with col4:
        cs = st.text_input('Compactness_se')

    with col5:
        Cs = st.text_input('Concavity_se')
    
    with col6:
        cps = st.text_input('Concave_points_se')

    with col1:
        Ss = st.text_input('Symmerty_se')

    with col2:
        fds = st.text_input('Fractal_D_se')

    with col3:
        rw = st.text_input('Radius_worst')

    with col4:
        tw = st.text_input('Texture_worst')

    with col5:
        pw = st.text_input('Perimeter_worst')
    
    with col6:
        aw = st.text_input('Area_worst')

    with col1:
        sw = st.text_input('Smoothness_worst')

    with col2:
        cw = st.text_input('Compactness_worst')

    with col3:
        Cw = st.text_input('Concavity_worst')

    with col4:
        cpw = st.text_input('Con_point_worst')

    with col5:
        Sw = st.text_input('Symmetry_worst')
    
    with col6:
        fdw = st.text_input('Fractal_D_worst')

    # code for Prediction
    breastcancer_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):

        user_input = [rm, tm, pm, am, sm,
                      cm, Cm, cpm, Sm, fdm, rs, ts,
                      ps, As, ss, cs, Cs, cps, Ss, fds, rw, tw,
                      pw, aw, sw, cw, Cw, cpw, Sw, fdw]

        user_input = [float(x) for x in user_input]

        breastcancer_prediction = breast_cancer_model.predict([user_input])

        if breastcancer_prediction[0] == 0:
            breastcancer_diagnosis = "The Breast cancer is Malignant"
        else:
            breastcancer_diagnosis = "The Breast Cancer is Benign"

    st.success(breastcancer_diagnosis)
    
   