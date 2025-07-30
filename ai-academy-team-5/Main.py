import streamlit as st

def main():
    if 'prev_page' not in st.session_state:
        st.session_state.prev_page = 'Home'

    st.set_page_config(
        page_title="School of Dandori Chatbot",
        page_icon="🐼",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 480px;
        color: #4B0082; /* Indigo */
    }
    
    .centered-subheader {
        text-align: center;
        font-size: 24px;
        color: #696969; /* Dim Gray */
    }
    
    .feature-header {
        font-size: 20px;
        color: #000080; /* Navy */
    }
    
    .feature-description {
        font-size: 16px;
        color: #2F4F4F; /* Dark Slate Gray */
    }
    
    .contact-info {
        text-align: center;
        font-size: 14px;
        color: #D3D3D3; /* Light Gray */
    }

    .team-header {
        font-size: 36px;
        color: #696969; /* Dim Gray */
        margin-bottom: 10px;
    }
    
    .member-name {
        font-size: 22px;
        color: #2F4F4F; /* Dark Slate Gray */
        margin: 10px 0 5px;
        text-align: center;
    }

    .member-role {
        font-size: 18px;
        color: #808080; /* Gray */
        text-align: center;
        margin-bottom: 5px;
    }

    .member-email {
        font-size: 16px;
        color: #1E90FF; /* Dodger Blue */
        text-align: center;
        margin-bottom: 15px;
    }
    
    .container {
        margin-top: 20px;
    }

    .divider {
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True
    )

    page_selection = st.navigation([
        st.Page("pages/Home.py", title = "Home ", icon = "🏠"),
        st.Page("pages/Chatbot.py", title = "DandoriBot ", icon = "🐼"),
        st.Page("pages/About.py", title = "About ", icon = "ℹ️"),
        st.Page("pages/FAQ.py", title = "FAQ ", icon = "❓"),
        st.Page("pages/Team.py", title = "Team ", icon = "🏢"),
        st.Page("pages/Settings.py", title = "Settings ", icon = "⚙️")
        ])
    page_selection.run()    

    if page_selection != st.session_state.prev_page:
        st.session_state.prev_page = page_selection
        st.balloons()

if __name__ == "__main__":
    main()