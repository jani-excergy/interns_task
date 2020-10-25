#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 06:19:17 2020

@author: manojkumar
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st



pickle_in = open("Random_classifier.pkl","rb")
random_forest_classifier=pickle.load(pickle_in)


def welcome():
    return " welcome all"



def predict_in_out(customer_since_months,max_return_days,avg_vas_count,avg_new_ads,avg_active_ads):
    
    
    prediction=random_forest_classifier.predict([[ customer_since_months,max_return_days,avg_vas_count,avg_new_ads,avg_active_ads]])
    print(prediction)
    return prediction 


def main():
    st.title("Customer IN or OUT from VAS service")
    html_temp = """
    <div style="background-color:green;padding:20px">
    <h2 style="color:white;text-align:center;"> ML APP </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    customer_since_months= st.text_input("customer_since_months","Type Here")
    max_return_days = st.text_input("max_return_days ","Type Here")
    avg_vas_count = st.text_input("avg_vas_count ","Type Here")
    avg_new_ads= st.text_input("avg_new_ads ","Type Here")
    avg_active_ads= st.text_input("avg_active_ads","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_in_out(customer_since_months,max_return_days,avg_vas_count,avg_new_ads,avg_active_ads)
    st.success('The output class is {}'.format(result))
    if st.button("About"):
        st.text("Janibasha Shaik")
        st.text(" 2020 ")

if __name__=='__main__':
    main()
