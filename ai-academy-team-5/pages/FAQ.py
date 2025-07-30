import streamlit as st

st.title("Frequently Asked Questions")

st.header("General Questions")

faq_items = {
    "What is Dandori?": "Dandori is the Japanese art of efficient task preparation and organization, focusing on planning ahead to optimize productivity.",
    "How can the Dandori Chatbot help me?": "The chatbot assists in understanding Dandori principles, provides productivity tips, and answers related questions to improve your organizational skills.",
    "Is there a cost to use the Dandori Chatbot?": "No, the Dandori Chatbot is free to use for all visitors.",
    "Which topics can the chatbot cover?": "The chatbot can address topics like task management, productivity strategies, and organizational principles rooted in Dandori."
}

for question, answer in faq_items.items():
    with st.expander(question):
        st.write(answer)

st.header("Technical Questions")

technical_faq_items = {
    "What should I do if the chatbot isn't responding?": "Ensure you have an active internet connection. Try refreshing your browser or clearing cache if issues persist.",
    "Can I access the chatbot from mobile devices?": "Yes, the Dandori Chatbot is accessible across all devices with internet capabilities.",
    "Is my data private and secure?": "Absolutely. We do not store any personal data entered during your interaction with the chatbot.",
}

for question, answer in technical_faq_items.items():
    with st.expander(question):
        st.write(answer)

st.markdown("---")
st.write("If you have further questions, feel free to contact us at [info@dandori.com](mailto:info@dandori.com).")