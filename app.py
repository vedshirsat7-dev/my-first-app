import streamlit as st

st.set_page_config(page_title="Meri Pehli App", page_icon="🚀")
st.title("🚀 Meri App Live Ho Gayi!")
st.write("Bhai deploy successful!")

name = st.text_input("Tera naam kya hai?")
if name:
    st.success(f"Welcome {name} bhai! 🔥")
