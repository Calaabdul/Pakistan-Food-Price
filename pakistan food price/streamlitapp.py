#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:54:25 2024

@author: dr.u.aajidagba
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import pickle 
import streamlit as st

file = 'ridge.pkl'
model = pickle.load(open(file, 'rb'))

st.title('Pakistan Food Price Prediction App')



def input():
    
    commodities = (
        'Rice',
        'Wheat',
        'Lentils',
        'Egg',
        'Milk',
        'Oil',
        'Sugar',
        'Ghee',
        'Beans',
        'Poultry',
        'Salt')
    categories = (
        'cereals and tubers',
        'pulses and nuts', 
        'milk and dairy',
        'oil and fats',
        'meat, fish and eggs',
        'miscellaneous food')
    
    
    
    cmname = st.selectbox('commodity', commodities)
    unit = st.selectbox('unit', ('KG', 'L', 'Dozen'))
    category = st.selectbox('category', categories)
    day= st.slider('Enter day', 1, 7)
    month = st.slider('Enter month', 1, 12)
    year = st.slider('Enter year', 2004, 2019)
    
    
    
    data = {'Name of Commodity':cmname,
            'unit': unit,
            'category': category,
            'day': day, 
            'month': month, 
            'year': year
            }
    
    features = pd.DataFrame(data, index = [0])
    return features


df = input()


def make_prediction():
    prediction = model.predict(df)
    print(f'the price is {prediction}')
    
if st.button('predict'):
    result = make_prediction()