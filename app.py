import streamlit as st  

st.title("Story Generator AI")  
st.write("Yahan par apni AI story generator app ka content add karein.")  

# Example input field
title = st.text_input("Enter Story Title:", "")

if st.button("Generate Story"):
    st.write(f"Generated Story for: {title}")
