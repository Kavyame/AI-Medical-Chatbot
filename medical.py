import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Configure Gemini AI
genai.configure(api_key="AIzaSyAoziICnuGNlejaqpuELbcvpEkSsXA5_HE")  # Replace with your actual API key


# Function to process image with Gemini AI
def analyze_medical_image(image):
    try:
        # Convert to PIL image if not already
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


# Streamlit UI
st.title("🩺 AI-Powered Medical Chatbot (Gemini AI Only)")

# Upload image for medical diagnosis
uploaded_image = st.file_uploader("Upload a medical image (X-ray, MRI, etc.)", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Fetching medical insights... Please wait!"):
        diagnosis_result = analyze_medical_image(image)

    st.success("✅ Diagnosis Result:")
    st.write(diagnosis_result)

# Chatbot section
st.subheader("💬 Ask Medical Questions")
user_query = st.text_input("Enter your medical question:")

if st.button("Get Answer"):
    with st.spinner("Processing..."):
        chatbot_response = get_medical_insights(user_query)
    st.success("✅ Chatbot Answer:")
    st.write(chatbot_response)
