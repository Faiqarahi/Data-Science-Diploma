import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open( "model.p", "rb" ))

def inputs(Age,KM,HP,CC,Gears,Quarterly_Tax,Weight):
    Age = float(Age)
    KM = float(KM)
    HP = float(HP)
    CC = float(CC)
    Gears = int(Gears)
    Quarterly_Tax = float(Quarterly_Tax)
    Weight = float(Weight)
    new_data=pd.DataFrame({'Age_08_04':Age,"KM":KM,"HP":HP, "cc":CC, 
                           "Gears":Gears, "Quarterly_Tax":Quarterly_Tax, "Weight":Weight},index=[1])
    final_predict = model.predict(new_data)
    return(final_predict).values

def main():
    
    st.title('Predicting car prices')
    '''#### Multiple Linear Regression Model'''
    '''Dataset : Toyoto Corolla'''
    '''@ Shrikant Uppin'''
    Age = st.text_input('Age')
    KM = st.text_input('KM')
    HP = st.text_input('HP')
    CC = st.text_input('CC')
    Gears = st.text_input('Gears')
    Quarterly_Tax = st.text_input('Quarterly_Tax')
    Weight = st.text_input('Weight')
    
    if st.sidebar.button('Predict'):
        output = inputs(Age,KM,HP,CC,Gears,Quarterly_Tax,Weight)
        st.success('the predicted car price is{}'.format(output))
   
if __name__=='__main__':
    main()