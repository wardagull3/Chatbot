import google.generativeai as genai
import streamlit as st

# Fetch the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["google"]["api_key"]
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def GetResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

st.set_page_config(page_title="Warda's AI Assistant", page_icon="🤖", layout="centered")

# Sidebar
st.sidebar.title("Settings")
st.sidebar.info("Configure settings or check updates here.")

# Main content
st.title("🤖 Warda's AI Assistant")
st.markdown("### Hi there! I'm Warda's Chatbot. How can I assist you today?")

user_input = st.text_input("Enter your question or request:", "")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Thinking... 🤔"):
            output = GetResponseFromModel(user_input)
            st.success("Here's what I found:")
            st.write(output)
    else:
        st.warning("Please enter something to ask!")

st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io/) and Google's Generative AI.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>input {
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
