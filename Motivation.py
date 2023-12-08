import streamlit as st

st.set_page_config(page_title = 'Motivation', page_icon = '💪', layout = "centered")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html = True)

col1, col2, col3 = st.columns([1, 1, 1])

video_html = """
            <video controls width="300" autoplay="true" loop="true">
            <source 
            src="https://drive.google.com/uc?export=download&id=1xXgLiWKS8b_7m7FqX2ZBnfXcq-qFgmft" 
            type="video/mp4" />
            </video>
            """
with col2:
    st.markdown(video_html, unsafe_allow_html = True)