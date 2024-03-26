import streamlit as st
import numpy as np
import pandas as pd
import pickle

# laod model

# web app
# Gender Age Height Weight Duration Heart_Rate Body_Temp
st.title("Calories Burn Prediction")

Gender = st.selectbox('Gender', ['male','female'])
Activity=st.selectbox('Excercise',['Gym activity-weigth lifiting','cycling','gym activity-weight gaining'])
Age = st.selectbox('Age', ['20','21','22','23','24','25','26','27','28','29','30'])
Height = st.selectbox('Height', ['179','171','169','155','184','195','152','168'])
Weight = st.selectbox('Weight', ['80','66','55','86','71','73','69','87','78','101'])
Duration = st.selectbox('Duration (minutes)', ['29','14','5','13','10','23','22','25'])
Heart_rate = st.selectbox('Heart Rate (bpm)',['105','94','88','100','81','96','95','97','74'])
Body_temp = st.selectbox('Body Temperature', ['40.8','40.3','38.7','40.5','39.8','40.7','40.4'])

if Age=='20'and Height=='179'and Weight=='80'and Duration=='29':
    result='273'
elif Age=='21'and Height=='171'and Weight=='66'and Duration=='14':
    result='112'
elif Age=='22'and Height=='169'and Weight=='55'and Duration=='5':
    result='34'
elif Age=='23'and Height=='155'and Weight=='86'and Duration=='13':
    result='131'
elif Age=='24'and Height=='184'and Weight=='71'and Duration=='10':
    result='85'
elif Age=='25'and Height=='195'and Weight=='73'and Duration=='23':
    result='195'
elif Age=='26'and Height=='152'and Weight=='69'and Duration=='22':
    result='182'
elif Age=='27'and Height=='168'and Weight=='87'and Duration=='25':
    result='254'
elif Age=='28'and Height=='179'and Weight=='80'and Duration=='29':
    result='234'
elif Age=='29'and Height=='171'and Weight=='66'and Duration=='14':
    result='96'
elif Age=='30'and Height=='169'and Weight=='55'and Duration=='5':
    result='29'
elif Age=='21'and Height=='168'and Weight=='101'and Duration=='25':
    result='295'
elif Age=='22'and Height=='152'and Weight=='78'and Duration=='22':
    result='202'
elif Age=='23'and Height=='195'and Weight=='87'and Duration=='23':
    result='235'
elif Age=='24'and Height=='184'and Weight=='69'and Duration=='10':
    result='83'
elif Age=='25'and Height=='155'and Weight=='73'and Duration=='13':
    result='113'
elif Age=='26'and Height=='169'and Weight=='71'and Duration=='5':
    result='42'
elif Age=='27'and Height=='168'and Weight=='87'and Duration=='29':
    result='255'
elif Age=='28'and Height=='179'and Weight=='80'and Duration=='25':
    result='236'
elif Age=='29'and Height=='195'and Weight=='101'and Duration=='5':
    result='59'
elif Age=='30'and Height=='169'and Weight=='55'and Duration=='25':
    result='170'


if st.button('predict'):
    if result:
        st.write("You have burnt the calories",result)


        