import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import pyttsx3
import speech_recognition as sr

# Configure Gemini AI (Replace with your actual API key)
genai.configure(api_key="YOUR_API_KEY")

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Function to analyze medical image
def analyze_medical_image(image):
    try:
        if not isinstance(image, Image.Image):
            image = Image.open(io.BytesIO(image.read()))

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(["Analyze this medical image", image])
        return response.text
    except Exception as e:
        return f"Error: {e}"


# Function to handle medical chatbot
def get_medical_insights(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"


# Function to convert text to speech
def speak_text(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(f"Error in text-to-speech: {e}")


# Function to handle voice input
def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech recognition service unavailable."


# Streamlit UI
st.set_page_config(page_title="AI Medical Chatbot", page_icon="🩺", layout="wide")
st.title("🩺 AI-Powered Medical Chatbot with Voice")
st.write("💡 Upload a medical image for analysis or ask medical-related questions.")

# Upload image for medical diagnosis
st.subheader("📷 Medical Image Analysis")
uploaded_image = st.file_uploader("Upload an X-ray, MRI, or other medical image:", type=["jpg", "jpeg", "png"],
                                  help="Upload an image for AI-based diagnosis.")

if uploaded_image:
    st.image(uploaded_image, caption="🖼️ Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Analyzing the image... Please wait!"):
        diagnosis_result = analyze_medical_image(uploaded_image)

    st.success("✅ Diagnosis Result:")
    st.write(diagnosis_result)

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🔊 Listen to Diagnosis"):
            speak_text(diagnosis_result)

st.markdown("---")  # Section Divider

# Chatbot section
st.subheader("💬 Medical Chatbot")

# Text input for chatbot
user_query = st.text_area("📝 Enter your medical question:", placeholder="Type your question here...", height=100)

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("🎤 Speak Your Question"):
        user_query = recognize_voice()
        st.text(f"🔹 You said: {user_query}")

with col2:
    if st.button("🤖 Get AI Answer"):
        with st.spinner("💭 Thinking..."):
            chatbot_response = get_medical_insights(user_query)
        st.success("✅ AI Response:")
        st.write(chatbot_response)

        if st.button("🔊 Listen to Answer"):
            speak_text(chatbot_response)

st.markdown(
    "💡 **Disclaimer:** This AI chatbot provides informational responses and should not be considered a substitute for professional medical advice.")
