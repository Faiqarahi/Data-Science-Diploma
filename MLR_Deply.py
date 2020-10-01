# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""

import pandas as pd
import streamlit as st 
import statsmodels.formula.api as smf

st.title('Model Deployment: MLR Regression')

st.sidebar.header('User Input Parameters')
#D:\Sri\Deployment\MLR_Deply\Cars.csv

def user_input_features():
    VOL = st.sidebar.number_input("Insert the VOL")
    SP = st.sidebar.number_input("Insert the SP")
    HP = st.sidebar.number_input("Insert the HP")    
    data = {'VOL':VOL,
            'SP':SP,
            'HP':HP}
    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

cars = pd.read_csv("D:\\Sri\\Deployment\\MLR_Deply\\Cars.csv")

#cars[cars.index.isin([70, 76])]

#Load the data
cars_new = pd.read_csv("D:\\Sri\\Deployment\\MLR_Deply\\Cars.csv")

#Discard the data points which are influencers and reasign the row number (reset_index())
car1=cars_new.drop(cars_new.index[[70,76]],axis=0).reset_index()

#Drop the original index
car1=car1.drop(['index'],axis=1)

#Exclude variable "WT" and generate R-Squared and AIC values
final_ml_V= smf.ols('MPG~VOL+SP+HP',data = car1).fit()

prediction = final_ml_V.predict(df)

st.subheader('Predicted Result')
#st.subheader('Prediction Probability')
st.write(prediction)
