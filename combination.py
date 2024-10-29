import streamlit as st

from math import comb

st.header ("Calculate profit on combinations")

# n	r	combin	inv per combin	inv total	coef avg	correct predic	correct combination	wrong combination	result	profit	potensial

col1, col2 = st.columns([1, 2])


n=int(col1.number_input('Number of items',value=1,min_value=1,))
r=int(col1.number_input('Size of group',value=1,min_value=1))


invest=col1.number_input('Investment per group',value=1.0,min_value=0.0,step=0.1)

preds=int(col1.number_input('Number of correct predictions',value=1,max_value=n,))
coefavg=col1.number_input('Coefficient',value=1.0,step=0.1)
# coefavg=st.slider('Average coefficient', min_value=1.0,max_value=20.0)
# print(n,r)
combin=comb(n,r)
invtotal=invest*combin

corcombination=comb(preds,r)
wrongcombination=combin-corcombination

def result():
    result=corcombination*invest*coefavg*r
    profit=result-invtotal
    resultsingle=invest*corcombination*coefavg
    profitsingle=resultsingle-invest*n
    combin=comb(n,r)
    # st.text(result)
    # st.write(str(result))
    # col2.write('smth')
    col2.subheader('Combinations (C): '+ str(combin))
    col2.subheader('Total investment: '+ str(round(invtotal,2)))
    col2.subheader('Total profit (C): '+ str(round(result,2)))
    col2.subheader('Net profit (C): '+ str(round(profit,2)),divider="gray")
    col2.subheader('Total profit single: '+ str(round(resultsingle,2)))
    col2.subheader('Net profit single: '+ str(round(profitsingle,2)),divider="gray")
    return result,profit


# Display calculated results
# st.write("Total Combinations:", combin)
# st.write("Total Investment Required:", invtotal)
result_value = result()



 
