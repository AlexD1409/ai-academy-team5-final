import streamlit as st

st.markdown('<p class="centered-title">Welcome to the Dandori Chatbot Experience</p>', unsafe_allow_html=True)
st.markdown('<p class="centered-subheader">Master the art of preparation and organization with our intelligent assistant.</p>', unsafe_allow_html=True)

st.image("background.jpeg")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("## Features", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1], gap="large")
with col1:
    st.markdown('<p class="feature-header">Productivity Tips 📈</p>', unsafe_allow_html=True)
    st.markdown('<p class="feature-description">Receive suggestions to improve your workflow and efficiency.</p>', unsafe_allow_html=True)

with col2:
    st.markdown('<p class="feature-header">Instant Answers ✅</p>', unsafe_allow_html=True)
    st.markdown('<p class="feature-description">Have your questions about Dandori principles answered promptly.</p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p class="feature-header">Resource Hub 🧠</p>', unsafe_allow_html=True)
    st.markdown('<p class="feature-description">Access a collection of resources for deeper learning.</p>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="contact-info">Contact us at info@dandori.com | © 2025 School of Dandori</p>', unsafe_allow_html=True)
