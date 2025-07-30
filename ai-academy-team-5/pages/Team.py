import streamlit as st
from PIL import Image

st.set_page_config(page_title="Meet the Team", page_icon="👥", layout="centered")

st.markdown('<p class="centered-title">Meet the Team!</p>', unsafe_allow_html=True)

st.markdown('<p class="team-header">Team Members</p>', unsafe_allow_html=True)

team_members = [
    {"name": "Max", "role": "Project Manager", "email": "max@example.com", "emoji": "👨‍💼"},
    {"name": "Alex", "role": "Software Engineer", "email": "alex@example.com", "emoji": "👨‍💻"},
    {"name": "Maya", "role": "Designer", "email": "maya@example.com", "emoji": "🎨"},
    {"name": "Will", "role": "Data Scientist", "email": "will@example.com", "emoji": "📊"}
]

for member in team_members:
    with st.container():
        col1, col2, col3, col4 = st.columns([1, 2, 3, 4])  
        
        with col1:    
            st.markdown(f'<p class="member-emoji">{member["emoji"]}</p>', unsafe_allow_html=True)

        with col2:         
            st.markdown(f'<p class="member-name">{member["name"]}</p>', unsafe_allow_html=True)

        with col3:
            st.markdown(f'<p class="member-role">{member["role"]}</p>', unsafe_allow_html=True)

        with col4:
            st.markdown(f'<p class="member-email">{member["email"]}</p>', unsafe_allow_html=True)

