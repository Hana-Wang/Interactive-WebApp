import streamlit as st
import pandas as pd

Year_List = [2, 3, 4, 5, 6, 7, 8, 9, 10]

st.write("""
# Compound Interest Calculator!

""")

st.sidebar.header('User Input Values')

def user_input_features():

    Int_Rate = st.sidebar.slider('Interest Rate in %', 6.0, 42.0, 10.0)

    Principal = st.sidebar.text_input('Please input Principal Amount',10000)

    No_Of_Years = st.sidebar.selectbox('Select No of Years', Year_List, 2)

    data = {'Int_Rate': Int_Rate,
            'Principal': Principal,
            'No_Of_Years': No_Of_Years}

    features = pd.DataFrame(data, index=[0])

    return features

df = user_input_features()


st.subheader('User Entered parameters for Rate, Principal amount and ')

st.write(df)


#Compound Interest function

def compound_int(Principal, Int_Rate, No_Of_Years):
    comp=1.0
    for i in range(0, int(No_Of_Years)):
        comp = comp * (1+Int_Rate/100)
    comp = float(Principal)*(comp-1)
    comp_text=str("Compound Interest is" + str("%.3f" % comp))
    st.write(comp_text)

    data_1 = {'Computed_Compoud_Interest': comp_text}

    result = pd.DataFrame(data_1, index=[0])

    return result


st.subheader('The calculated compound interest is')

df_1 =  compound_int(df.Principal, df.Int_Rate, df.No_Of_Years)


st.subheader('This is print of data frame')

st.write(df_1)
