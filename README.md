# 🩺 AI-Powered Medical Chatbot with Voice

An AI-powered medical chatbot built with **Python, Streamlit, and Google Gemini AI**. The application allows users to ask medical-related questions, upload medical images for AI-based analysis, and interact with the chatbot using voice input and text-to-speech.

## ✨ Features

* 🩺 **Medical Chatbot** – Ask medical-related questions and receive AI-generated responses.
* 📷 **Medical Image Analysis** – Upload X-rays, MRI scans, or other medical images for AI-based analysis.
* 🎤 **Voice Input** – Ask questions using your microphone.
* 🔊 **Text-to-Speech** – Listen to the AI-generated responses.
* 💻 **Interactive Streamlit Interface** – Simple and user-friendly web interface.
* ⚠️ **Medical Disclaimer** – Responses are intended for informational purposes only and are not a substitute for professional medical advice.

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Google Gemini AI**
* **Pillow (PIL)**
* **PyAudio / SpeechRecognition**
* **pyttsx3**

## 📂 Project Structure

```text
AI-Medical-Chatbot/
│
├── f3.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Medical-Chatbot.git
cd AI-Medical-Chatbot
```

### 2. Install the required libraries

```bash
pip install streamlit google-generativeai pillow pyttsx3 SpeechRecognition
```

### 3. Configure the Gemini API Key

In `f3.py`, configure your Google Gemini API key:

```python
genai.configure(api_key="YOUR_API_KEY")
```

**Do not upload your real API key to GitHub.**

For a public repository, it is recommended to store the API key in an environment variable instead.

## ▶️ Run the Application

Run the following command in the terminal:

```bash
streamlit run f3.py
```

The application will open in your web browser.

## 🔄 How It Works

### Medical Image Analysis

1. Upload a medical image such as an X-ray or MRI image.
2. The image is sent to the Gemini AI model.
3. Gemini analyzes the uploaded image.
4. The generated response is displayed in the Streamlit application.
5. The user can listen to the response using text-to-speech.

### Medical Chatbot

1. Enter a medical-related question.
2. Click **Get AI Answer**.
3. Gemini generates a response.
4. The response is displayed on the screen.
5. The response can also be converted into speech.

### Voice Interaction

1. Click **Speak Your Question**.
2. Speak through the microphone.
3. SpeechRecognition converts the voice into text.
4. The converted question is sent to Gemini AI.
5. The AI-generated response is displayed.

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
google-generativeai
Pillow
pyttsx3
SpeechRecognition
```

Depending on your operating system, **PyAudio** may also be required for microphone input.

## ⚠️ Disclaimer

This application is an **AI-based informational tool** and is not intended to provide professional medical diagnosis or treatment. AI-generated responses may be inaccurate. Users should consult a qualified healthcare professional for medical advice, diagnosis, or treatment.

## 🚀 Future Enhancements

* 🔐 Secure API key management using `.env`
* 🧑‍⚕️ Integration with verified medical knowledge sources
* 📄 Support for PDF medical reports
* 💾 Chat history
* 🌐 Multilingual voice interaction
* 👨‍⚕️ Doctor consultation integration
* 📊 Improved medical image analysis
* 🔒 User authentication and secure data handling

## 👩‍💻 Author

**Kavya Dutta**

Computer Science and Engineering
