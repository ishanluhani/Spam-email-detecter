import streamlit as st
import joblib

model = joblib.load('model.pkl')
feature_extraction = joblib.load('feature_extraction.pkl')
st.title('Spam and Not Spam Detector by ishan luhani')
form = st.form('email_detector')
mail = form.text_input('Write mail here: ')
n = False
if form.form_submit_button(label='Submit'):
    n = not n
    form.write('Spam' if model.predict(feature_extraction.transform([mail])) else 'Not Spam')