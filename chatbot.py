import streamlit as st
import google.generativeai as genai
import os
# Configure the API key (fetch it from Streamlit secrets)
GOOGLE_API_KEY = st.secrets["google"]["api_key"]
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="Warda's AI Assistant", page_icon="🤖", layout="centered")

# Custom CSS to fix the input field at the bottom and make the chat area scrollable
st.markdown("""
    <style>
    .stApp {
        display: flex;
        flex-direction: column;
        height: 100vh;
    }
    .chat-history {
        flex-grow: 1;
        overflow-y: auto;
        padding: 10px;
    }
    .chat-input {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 10px 0;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
        z-index: 1;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Warda's AI Assistant")
st.write("Hi there! I'm Warda's Chatbot. How can I assist you today?")

# Initialize chat history in session state if not already present
if "history" not in st.session_state:
    st.session_state["history"] = []

# Chat history container with scrollable area
with st.container():
    st.markdown('<div class="chat-history">', unsafe_allow_html=True)
    if st.session_state.history:
        for user_message, bot_message in st.session_state.history:
            st.markdown(f"""
            <div style="
                background-color: #d1d3e0;
                border-radius: 15px;
                padding: 10px 15px;
                margin: 5px 0;
                max-width: 70%;
                text-align: left;
                display: inline-block;
            ">
                <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
                background-color: #e1ffc7;
                border-radius: 15px;
                padding: 10px 15px;
                margin: 5px 0;
                max-width: 70%;
                text-align: left;
                display: inline-block;
            ">
                <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Input form fixed at the bottom
with st.form(key="chat_form", clear_on_submit=True):
    st.markdown('<div class="chat-input">', unsafe_allow_html=True)
    user_input = st.text_input("💬 Enter your question or request:", max_chars=2000)
    submit_button = st.form_submit_button("Send")
    st.markdown('</div>', unsafe_allow_html=True)

    if submit_button and user_input:
        # Get the chatbot response
        response = get_chatbot_response(user_input)
        # Append the input and response to the session history
        st.session_state.history.append((user_input, response))
        # The input field is cleared automatically by `clear_on_submit=True`
