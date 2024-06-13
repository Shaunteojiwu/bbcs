import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
st.set_page_config(page_title="Are you ready for retirement?", page_icon="💰", layout="wide")

st.title("Welcome to an app the estimates your retirement age")
st.write("Lets find out if your actual retirement age matches your ideal")

st.text_input("Age","Input your present age")
option = st.selectbox("What is your current housing type?",["2-room","3-room","4-room","5-room","Executive HDB","Executive condomimium","Terrace","Semi-detached house","Bungalow","Others"])

income = st.number_input("Enter your yearly income:")
expenditure = st.number_input("Enter your yearly expenditure:")

if st.button("Calculate"):
    savings = income - expenditure 
    if savings > 0:
        st.success(f"You are saving {savings} units per month.")
    else:
        st.error("Your yearly expenditure exceeds your yearly income. This will increase your retirement age")
        
if quality_of_life >= 5:
     print ("You're living life!")
else:
    print ("Life is not looking good,seek help")

if disaster_preparedness>5:
    print ("You should be fine in any cases of emergencies")
else:
    print ("You are not prepared for emergencies")
if retirement_readiness>5:
    print("You will retire at your ideal age")
else:
    print("You will be able to retire at your ideal age")
    

    
st.slider("On a scale of 1-10, rate your quality of life?",0,10,5)
if QOL >=7:
    st.write("You're lving life!")
elif QOL>=5:
    st.write("Life can be better")
else: 
    st.write("Life is not looking good,we will try out best to help")
