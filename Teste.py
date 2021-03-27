import streamlit as st
import pandas as pd

st.title('Olá amigo')
st.write('É nóis truta')
st.write(pd.DataFrame({
    'primeira': [1,2,3],
    'segunda': [4,5,6]
    
}))

