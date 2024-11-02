import streamlit as st
from math import comb

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",)
st.header ("Calculate profit on combinations")


for i in st.secrets.items():
    print(i)

print('hi')
# Initialize session state variables for dynamic updates
if 'n' not in st.session_state:
    st.session_state['n'] = 1
if 'r' not in st.session_state:
    st.session_state['r'] = 1
if 'invest' not in st.session_state:
    st.session_state['invest'] = 1.0
if 'coefavg' not in st.session_state:
    st.session_state['coefavg'] = 1.0
if 'preds' not in st.session_state:
    st.session_state['preds'] = 1

def update_n(val):
    st.session_state['n']=val
def update_r(val):
    st.session_state['r']=val
def update_invest(val):
    st.session_state['invest']=val
def update_preds(val):
    st.session_state['preds']=val
def update_coef(val):
    st.session_state['coefavg']=val

# with st.container():

col1, col4 = st.columns([2,2],gap="small",vertical_alignment="bottom")
with col1:
    
    # st.write(st.session_state.n)
    with st.container():
        col11,col12,col13 = st.columns([2,1,1],vertical_alignment="bottom")
        with col11:                
            n=st.number_input('Number of items',value=st.session_state['n'],min_value=1,key='n')
        with col12:
            n10=st.button('10',on_click=update_n,args=[10],use_container_width=True)
        with col13:
            n5=st.button('5',on_click=update_n,args=[5],use_container_width=True)
        
    with st.container():
        col14,col15,col22 = st.columns([2,1,1],vertical_alignment="bottom")
        if st.session_state['r']>st.session_state['n']:
            st.session_state['r']=st.session_state['n']  
        with col14:
            r=int(st.number_input('Size of group',value=st.session_state['r'],min_value=1,max_value=n))
        with col15:
            nmax=st.button('max',on_click=update_r,args=[n],use_container_width=True)
        with col22:
            nmin=st.button('min',on_click=update_r,args=[1],use_container_width=True)    

    with st.container():
        col16,col17,col18 = st.columns([2,1,1],vertical_alignment="bottom")
        with col16:                
            invest=st.number_input('Investment per group',value=st.session_state['invest'],min_value=0.0,step=2.0)
        with col17:
            n102=st.button('10',on_click=update_invest,args=[10.0],use_container_width=True,key='invest10')
        with col18:
            n52=st.button('5',on_click=update_invest,args=[5.0],use_container_width=True,key='invest5')

    with st.container():
        col19,col20,col21 = st.columns([2,1,1],vertical_alignment="bottom")
        if st.session_state['preds']>st.session_state['n']:
            st.session_state['preds']=st.session_state['n']
        with col19:                
            preds=int(st.number_input('No. of correct predictions',value=st.session_state['preds'],max_value=n,))
        with col20:
            predsmax=st.button('max',on_click=update_preds,args=[n],use_container_width=True,key='predsmax')
        with col21:
            predsmin=st.button('min',on_click=update_preds,args=[1],use_container_width=True,key='predsmin')

        if st.session_state['preds']>st.session_state['n']:
            st.session_state['preds']=st.session_state['n']

    with st.container():
        col22,col23,col24,col25 = st.columns([2,1,1,1],vertical_alignment="bottom",gap='small')    
        with col22:
            coefavg=st.number_input('Coefficient',value=st.session_state['coefavg'],min_value=1.0,step=0.2)
        with col23:
            coef17=st.button('1.7',on_click=update_coef,args=[1.7],use_container_width=True,)
            
        with col24:
            coef3=st.button('3.0',on_click=update_coef,args=[3.0],use_container_width=True,)
        with col25:
            coef3=st.button('10.0',on_click=update_coef,args=[10.0],use_container_width=True,)
        
        
# coefavg=st.slider('Average coefficient', min_value=1.0,max_value=20.0)
# print(n,r)

def result():
    combin=comb(n,r)
    invtotal=invest*combin
    corcombination=comb(preds,r)
    wrongcombination=combin-corcombination
    result=corcombination*invest*coefavg*r
    profit=result-invtotal
    resultsingle=invest*preds*coefavg
    profitsingle=resultsingle-invest*n
    combin=comb(n,r)
    # st.text(result)
    # st.write(str(result))
    # col2.write('smth')

    col4.subheader('Combinations (C): '+ str(combin))
    col4.subheader('Total investment: '+ str(round(invtotal,2)))
    col4.subheader('Total profit (C): '+ str(round(result,2)))
    col4.subheader('Net profit (C): '+ str(round(profit,2)),divider="gray")
    col4.subheader('Total profit single: '+ str(round(resultsingle,2)))
    col4.subheader('Net profit single: '+ str(round(profitsingle,2)),divider="gray")

    st.sidebar.subheader('Combinations (C): '+ str(combin))
    st.sidebar.subheader('Total investment: '+ str(round(invtotal,2)))
    st.sidebar.subheader('Total profit (C): '+ str(round(result,2)))
    st.sidebar.subheader('Net profit (C): '+ str(round(profit,2)),divider="gray")
    st.sidebar.subheader('Total profit single: '+ str(round(resultsingle,2)))
    st.sidebar.subheader('Net profit single: '+ str(round(profitsingle,2)),divider="gray")

    return result,profit

def send_feedback():
    # send telegram message:
    api_key=st.secrets["api_key"]
    my_user_id=st.secrets["my_user_id"]
    params={'chat_id':my_user_id,'text':f'{comments} \n {selected} star(s) '}
    requests.get("https://api.telegram.org/bot{}/sendMessage".format(api_key), params=params)


result_value = result()

with st.sidebar.expander("Send review"):


    with st.form("my_form",clear_on_submit=True):
            
            # st.write("Send your comment")
            comments = st.text_area('Write your comment')

            sentiment_mapping = ["one", "two", "three", "four", "five"]
            selected = st.feedback("stars")
            if selected is not None:
                st.markdown(f"Thanks!")
                
            else:
                selected=3
                st.markdown(f"Thanks for your comments!")
                # sentiment_mapping[selected]='no star'
            selected=selected
        

            submitted = st.form_submit_button("Submit",on_click=send_feedback)




 
