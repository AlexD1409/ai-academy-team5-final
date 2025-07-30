import streamlit as st 
import os
from utility import load_prompt, save_prompt

settings_file = os.path.join(os.getcwd(), 'system.txt')

current_prompt = load_prompt(settings_file)

st.markdown('<p class="centered-title">Current Chatbot personality</p>', unsafe_allow_html=True)
st.text_area("System Prompt:", current_prompt, height=200, key='prompt_area')

if st.button("Save System Prompt"):
    updated_prompt = st.session_state['prompt_area']
    save_prompt(settings_file, updated_prompt)
    st.success("System prompt updated successfully!")
