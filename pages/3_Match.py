import streamlit as st
from sentence_transformers import util
import pandas as pd

model = st.session_state.model


def calc_similarity(t_sent, db_sents):
  #Compute embeddings
  embeddings = model.encode(db_sents, convert_to_tensor=True)
  embed = model.encode(t_sent, convert_to_tensor=True)

  #Compute cosine-similarities for each sentence with each other sentence
  cosine_scores = util.cos_sim(embed, embeddings)

  #Find the pairs with the highest cosine similarity scores
  pairs = []
  for i in range(len(cosine_scores)):
    for j in range(i, len(cosine_scores[0])):
      pairs.append({'index': [i, j], 'score': cosine_scores[i][j]})

  #Sort scores in decreasing order
  pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)
  return pairs


st.title("Match Users With Similar Problem")

btn = False
df = st.session_state.df
list_users = df["name"].tolist()
list_problems = df["problem"].tolist()

#Menu
with st.sidebar:
  name = st.text_input('type your name...', '', placeholder='name')
  name = [name]
  problem = st.text_area('define your problem...', '', placeholder='problem')
  problem = [problem]
  if st.button('Find people like me'):
    #Trigger calculation
    btn = True

res_users = []
res_problems = []

if btn:
  st.write("")
  pairs = calc_similarity(problem, list_problems)
  for pair in pairs[0:16]:
    i, j = pair['index']
    print("{} \t\t {} \t\t Score: {:.4f}".format(name[i], list_users[j], pair['score']))
    res_users.append([name[i], list_users[j], float(pair['score'])])
    print("{} \t\t {} \t\t Score: {:.4f}".format(problem[i], list_problems[j], pair['score']))
    res_problems.append([problem[i], list_problems[j], float(pair['score'])])
  
  pd_users = pd.DataFrame(res_users, columns = ['new_user', 'existing_usrs', 'score'])
  pd_problems = pd.DataFrame(res_problems, columns = ['new_problem', 'existing_problems', 'score'])
  st.write(pd_users)
  st.write(pd_problems)


   

