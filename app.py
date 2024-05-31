import streamlit as st
import pickle
import pandas as pd
import numpy as np
df=pd.read_csv("steam_data.csv")
appids=df['appid'].values
def recommend(game):    
    idx=games[games['name']==game].index[0]
    distances=similarity[idx]
    games_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    return games_list
games_list=pickle.load(open('games_dict.pkl','rb'))
similarity = np.load('similarity.npy', mmap_mode='r')
games=pd.DataFrame(games_list)
st.title("Video Game Recommender System")
option=st.selectbox(
    'Enter Game Name',
    games['name'].values
)
if st.button("Recommend"):
    my_options=recommend(option)
    #print(my_options)
    for i in my_options:
        name=games.iloc[i[0]]['name']
        #print(name)
        j=df[df['name']==name]['appid'].values[0]
        st.image(f"https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/{j}/header.jpg", caption=name, use_column_width=True)
        st.write()
        #st.write(games.iloc[i[0]]['name'])
