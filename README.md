
# 🌾 AgriGen AI

**Smart Agriculture Assistant powered by Generative AI**

---

## 📌 Overview

**AgriGen AI** is an intelligent conversational assistant designed to provide **practical farming and agriculture guidance**.
Built using **Streamlit**, it leverages a modular GenAI pipeline with **context memory**, **prompt engineering**, and **LLM integration (Gemini API)** to deliver accurate, context-aware responses for farmers and agronomy teams.

---

## 🚀 Features

* 💬 **Interactive Chat Interface** (modern UI with custom styling)
* 🧠 **Conversation Memory** for context-aware responses
* 🌱 **Agriculture-Focused Intelligence** (crops, soil, pests, irrigation)
* ⚡ **LLM Integration** (Gemini API via custom client)
* 🔄 **Reset Conversation** functionality
* 🎯 **Predefined Example Questions** for quick start
* 🎨 **Enhanced UI/UX** with gradient background & responsive layout

---

## 🏗️ Project Structure

```bash
AgriGen-AI/
│
├── app.py                  # Main Streamlit application
│
├── chatbot/
│   ├── gemini_client.py   # Gemini API integration
│   ├── memory_manager.py  # Conversation memory handling
│   ├── prompt_builder.py  # Prompt engineering logic
│
├── utils/                 # (Optional utilities)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agrigen-ai.git
cd agrigen-ai
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Libraries

* streamlit
* Gemini API client (custom implementation)
* (Optional)

  * pypdf
  * ReportLab

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

### 1. User Input

User asks a farming/agriculture-related question via chat.

### 2. Memory Management

* Stores conversation history
* Enables context-aware responses

### 3. Prompt Building

* Formats user input into structured prompt

### 4. LLM Processing

* Sends prompt + history to Gemini API
* Generates intelligent response

### 5. UI Rendering

* Displays chat using Streamlit chat components

---

## 💡 Example Questions

* What are the best practices for maize irrigation?
* How can I improve soil fertility organically?
* How to control pests in vegetable crops?
* Climate-smart farming techniques for small farms

---

## 🎨 UI Highlights

* Gradient background for better UX
* Sidebar with guided prompts
* Card-style layout for clean structure
* Chat-style interaction similar to modern AI apps

---

## 🔁 Session State Management

Uses Streamlit session state:

```python
st.session_state.memory   # stores chat history
st.session_state.client   # handles API calls
```

---

## 🧹 Reset Conversation

Clears chat memory instantly:

```python
st.session_state.memory.clear_memory()
st.experimental_rerun()
```

---

## 📌 Use Cases

* Farmers seeking crop guidance
* Agriculture students learning concepts
* Agronomy teams for quick insights
* Sustainable farming advisory

---

## ⚠️ Limitations

* Depends on external LLM (Gemini API)
* Responses may vary based on prompt quality
* Not a substitute for expert agricultural consultation

---

## 🔮 Future Improvements

* 🌐 Multilingual support (Marathi/Hindi)
* 📊 Crop analytics dashboard
* 📄 PDF export of advisory
* 🎙️ Voice-based interaction
* ☁️ Deployment (Streamlit Cloud / AWS)

---

## 👨‍💻 Author

**Pruthviraj Patil**
AI/ML & Data Analytics Enthusiast

---

## 📜 License

This project is for educational and portfolio purposes.

---
