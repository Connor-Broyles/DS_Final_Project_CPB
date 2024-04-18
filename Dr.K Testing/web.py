# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:25:09 2024

@author: Connor
"""

#importing libaries 

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
wine_quality = fetch_ucirepo(id=186) 
  
# data (as pandas dataframes) 
X = wine_quality.data.features 
y = wine_quality.data.targets 
  
# metadata 
print(wine_quality.metadata) 
  
# variable information 
print(wine_quality.variables) 

#incorporating a combination of both data sets
df = pd.read_csv("wq.csv")

#making a chemical data variable
chem = df[["Red_Wine","fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates"]]
alc = df[["Red_Wine","alcohol"]]
qual = df[["Red_Wine","quality"]]
#Starting the website
st.title(":wine_glass: :red[Wine Quality Viewer] :wine_glass:")

#Making tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Meta Data", "Data","Color","Quality","Scatter","Box","Classification",])

with tab1:
    st.header("Meta Data")
    st.dataframe(df)
    
with tab2:
    st.header("Data Set Viewer")
    #starting the button selection
    bt = st.radio(
        "Please Select Which portion of data you would like",
        ["Pick One","Chemical","Alcohol","Quality","All"])
    if bt == "Pick One":
        st.write("Please Pick a Button")
    elif bt == "Chemical":
        st.dataframe(chem)
    elif bt == "Alcohol":
        st.dataframe(alc)
    elif bt == "Quality":
        st.dataframe(qual)
    elif bt == "All":
        st.dataframe(df)
with tab3:
    st.header("Color Distribution")   
    
with tab4:
    st.header("Quality Distribution")
    
with tab5:
    st.header("Scatter Plots")
    
with tab6:
    st.header("Box Plots")
    
with tab7:
    st.header("Classification")

