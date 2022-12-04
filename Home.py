import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
import io

st.set_page_config(layout="wide")


@st.cache(persist=True, allow_output_mutation=True)
def retrieve_model():
    model_dir = "model"
    model = SentenceTransformer(model_dir)
    return model


st.session_state.model = retrieve_model()
st.session_state.df = None

st.title('Homepage')
st.text("This is a testing environment for matchmaking process.")

