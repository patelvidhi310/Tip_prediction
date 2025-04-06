import streamlit as st
import pandas as pd
import numpy as np
import pickle
# streamlit/ flask / django/ fastapi/ aws/ heroku/ gcp/ azure/nodejs
st.title("My Tip_prediction Streamlit App")
model=pickle.load(open('tip_prediction_lr.pkl','rb'))
# predict a particlular table tip
# Male is paying, he is smoker, doing dinner, size is 5 total bill is 100 $, 
# day is Saturday

user_input={}
st.subheader('User has to fill the table details to predict the tip')
user_input['total_bill'] = st.number_input('total_bill')
user_input['size'] = st.number_input('size')

st.subheader("user has to fill 1 if ts male else 0")
user_input['sex_Male'] = st.number_input('sex_Male') 
st.subheader("user has to fill 1 if ts female else 0")
user_input['sex_Female'] = st.number_input('sex_Female')
st.subheader("user has to fill 1 if ts smoker else 0")    
user_input['smoker_Yes'] = st.number_input('smoker_Yes')
st.subheader("user has to fill 1 if ts non smoker else 0")
user_input['smoker_No'] = st.number_input('smoker_No')
st.subheader("user has to fill 1 if ts thursday else 0")
user_input['day_Thur'] = st.number_input('day_Thur')
st.subheader("user has to fill 1 if ts friday else 0")
user_input['day_Fri'] = st.number_input('day_Fri')
st.subheader("user has to fill 1 if ts saturday else 0")
user_input['day_Sat'] = st.number_input('day_Sat')

st.subheader("user has to fill 1 if ts sunday else 0")
user_input['day_Sun'] = st.number_input('day_Sun')
st.subheader("user has to fill 1 if ts lunch else 0")
user_input['time_Lunch'] = st.number_input('time_Lunch')
st.subheader("user has to fill 1 if ts dinner else 0")
user_input['time_Dinner'] = st.number_input('time_Dinner')


user_input=pd.DataFrame(user_input,index=[0])
st.write(user_input)
if st.button('Predict'):
    output=model.predict(user_input)
    st.success(f'The predicted tip is {output[0]}')

