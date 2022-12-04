import streamlit as st
import pandas as pd

st.title("Upload Database Here")
st.caption("Accepted file is .csv with two column names:  [name, problem]")


#print(st.session_state.model)
@st.cache(persist=True)
def load_data(file):
    return pd.read_csv(file)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    
    st.session_state.df = load_data(uploaded_file)

if st.session_state.df is not None:
    st.write(st.session_state.df)
