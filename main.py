import streamlit as st
import pandas as pd

st.title('Olá')
st.write('É nóis Truta')
st.write(pd.DataFrame({
    'primeira': [1,2,3],
    'segunda': [4,5,6]
    
}))

