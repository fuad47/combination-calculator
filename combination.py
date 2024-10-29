import streamlit as st
import pandas as pd
import numpy as np
import time
import requests
from bs4 import BeautifulSoup
from math import comb

st.header ("Calculate profit on combinations")

# n	r	combin	inv per combin	inv total	coef avg	correct predic	correct combination	wrong combination	result	profit	potensial


n=int(st.number_input('Number of items',value=1,min_value=1,))
r=int(st.number_input('Size of group',value=1,min_value=1))


invest=st.number_input('Investment per group',value=1.0,min_value=0.0,step=0.1)

preds=int(st.number_input('Number of correct predictions',value=1,max_value=n,))
coefavg=st.number_input('Average coefficient',value=1.0,step=0.1)
# coefavg=st.slider('Average coefficient', min_value=1.0,max_value=20.0)
# print(n,r)
combin=comb(n,r)
invtotal=invest*combin

corcombination=comb(preds,r)
wrongcombination=combin-corcombination

def result():
    result=corcombination*invest*coefavg*r
    profit=result-invtotal
    combin=comb(n,r)
    # st.text(result)
    # st.write(str(result))
    st.subheader('Total combinations: '+ str(combin))
    st.subheader('Total investment: '+ str(round(invtotal,2)))
    st.subheader('Total profit: '+ str(round(result,2)))
    st.subheader('Net profit: '+ str(round(profit,2)))
    return result,profit


# Display calculated results
# st.write("Total Combinations:", combin)
# st.write("Total Investment Required:", invtotal)
result_value = result()
# st.text('hi')
# st.subheader('Total profit: ',str(result))



