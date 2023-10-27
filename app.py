import streamlit as st
import pandas as pd
import urllib3
import urllib 
import requests
from urllib.request import urlopen



def get_bookdata():
    url="https://drive.google.com/file/d/1nPqkspdr4l_BZf6mo4rShBkxVOohg251/view?usp=sharing"
    response = urllib.request.urlopen(url)
    df = pd.read_csv("도서정보2.csv", encoding='cp949')
    return df.set_index("책제목")

    

try:
    urllib.request.urlopen("https://drive.google.com/file/d/1nPqkspdr4l_BZf6mo4rShBkxVOohg251/view?usp=sharing")
    df = get_bookdata()
    bookSelect = st.multiselect(
        label="책이름을 입력하세요", options=list(df.index), default=["우리 집 늙은 고양이가 하는 말"]
    )
    if not bookSelect:
        st.error("하나의 책을 선택해주세요")
    else:
        data = df.loc[bookSelect]
        st.write(bookSelect, data.sort_index())

        data = data.T.reset_index()
        
    

     
except urllib.error.URLError as e:# use 'urllib.error.URLError' and not 'urllib.HTTPError'
        print ('Error code: ', e.code)# or what ever u want 
        
    
    
    
    
