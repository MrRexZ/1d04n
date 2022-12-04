import streamlit as st
import os
import requests
import shutil
from sentence_transformers import SentenceTransformer

st.set_page_config(layout="wide")


@st.cache(persist=True, allow_output_mutation=True)
def retrieve_model():
    presigned_url = "https://peraturan.s3.ap-southeast-3.amazonaws.com/output/model.zip?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLXNvdXRoZWFzdC0xIkYwRAIgf1lOB3%2FFjn0R0qrE1QPew1Tk7JDRJNn6%2BuoK%2FehBzlECIA2qOcZGyhG%2BZDrVEIdJBcs7LBkKM7pZDxzH0mJ%2FVwzwKo4DCNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMNzU1NzQ2MzQ4MTM1IgworB0cNUrTSsbn0jAq4gLLmqTcQxCQDq28foihbzgEp7SE1vSwgmoL8VOe7gRns49of4Kgw13mdUwniZ01MeJNpwT40HvPFxnzPYP4DeBmOOrK1R9aU%2BBgTA%2FgZVue7APASOpE95lhCMiKshERD4aKTWryH2vqD7UjiYNG1ya47BtzOHwDxNm2ygEfkY9v9F3aA1K%2BqY2urEMB4YIvLFD6Kp52YChtkX%2BHynzJ8u7AN1MkFCXWv05LR4BsEppYlq%2B4OaJMo6FhQWkokFRMpObAY0PW1IjUGK%2Bb%2BthFKc50ILeaue%2BkQX5gVCL6pgoMcNiWCYk8d%2ByHHBL6o0SR%2FDOT7DvHIL3JjpKghQ7joxf6YiogcMMdCtNUY5vmxNydvqVRvMV20IhGEknmveW%2BgTf3pWAeNzDFN7SesKCW65HfVkptlcSw2DCgbLyvjASWPCVQJQ2t7zV4Fw6c8qH6pekJFa8T2XK%2F7qh2dq4yeUTyImQwnYiznAY6tAKX9aQvr%2F3O%2FEs%2B0LPVgmiFy1K0zHCrywz1Ti29f2vXPS3vd8opEPu%2FZUp6PsqOsL9OMxcxVQMRP2YjetcirKWLHqG%2FM1ViLb1nrYVXgL4Mqb%2Fm%2FoifnEXjLSnKWl3HHcQ2UZ8hCbbNwswrVfenLLbSHpwQAVygFvaBMwfijhogpl0cZD%2FWd4DXfFLjP3zqI4iLbHTyq5%2FrT4xZyCb%2Bx5Y1gf3jAFR375V%2FdAAzxbUkly%2FFnCFRIWd0dDUi4hZKUHhHKvDQwYYgmJsqcwEMXiJk%2FyJ%2Bc3kzUBEZj6aB9mErkEXEHzII7GK4JuJtjE9H74eSowqABxCF7p8ogHBPfUSrZ%2BSq%2BaW%2FHLWuEdNnCgnl6qqo1QS%2BxLsycEwTSeKP%2BsuG1niRNp4ukuKudzDgmcgA2aIV%2FA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221204T160757Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIA275P6DRTYU5A3SUL%2F20221204%2Fap-southeast-3%2Fs3%2Faws4_request&X-Amz-Signature=6f97a0836f935f018535e83ccdad2146b0044887c363bdd5bf70dc515a3fa87e"
    model_zipped = "model.zip"
    model_dir = "model"

    if os.path.isfile(model_zipped) or os.path.isdir(model_dir):
        with open(model_zipped, 'wb') as out_file:
            content = requests.get(presigned_url, stream=True).content
            out_file.write(content)

        shutil.unpack_archive(filename=model_zipped, extract_dir=model_dir, format='zip')

    model = SentenceTransformer(model_dir)
    return model


st.session_state.model = retrieve_model()
st.session_state.df = None

st.title('Homepage')
st.text("This is a testing environment for matchmaking process.")

