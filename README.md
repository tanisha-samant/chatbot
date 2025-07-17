# chatbot

```markdown
# 🤖 Streamlit ChatBot – NLTK-Based ChatGPT-Style Assistant

This is a simple, intelligent chatbot web application built using **Python**, **NLTK**, and **Streamlit**. It simulates human-like conversations using a set of predefined intents and responses.

---

## 📌 Features

- 🧠 Basic NLP using NLTK
- 💬 ChatGPT-style interface with Streamlit
- 🗂️ Predefined intents and responses (stored in JSON)
- 🔄 Easily customizable and extendable
- ✅ Runs in GitHub Codespaces or locally

---

## 🧠 Technologies Used

- Python 3.x
- NLTK (Natural Language Toolkit)
- Streamlit
- JSON

---

## 📁 Project Structure


chatbot-nltk/
├── app.py               # Streamlit app – Chat interface
├── chatbot.py           # Core NLP logic and intent matching
├── intents.json         # Intents: questions and responses
├── requirements.txt     # Python dependencies
└── README.md            # Project readme


---

## 🚀 Getting Started

You can run this chatbot in your local environment or on GitHub Codespaces.

### 🟢 Clone the Repository

```bash
git clone https://github.com/your-username/chatbot-nltk.git
cd chatbot-nltk
````

### 🟢 Install Dependencies

Make sure Python 3 is installed. Then run:

```bash
pip install -r requirements.txt
```

### 🟢 Download NLTK Data

In Python shell:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

### 🟢 Run the ChatBot

```bash
streamlit run app.py
```

Streamlit will open the chatbot in your browser at:
`http://localhost:8501`

---

## 💬 Supported Intents

Some topics the chatbot understands:

* Greetings (`hi`, `hello`, `hey`)
* Goodbye (`bye`, `see you`)
* Thanks
* Jokes & Fun Facts
* Help, Motivation, Advice
* Time & Date
* Food, Study, Sleep Tips
* Programming Help
* Mental Health Support
* More…

Want to add your own? Just edit the `intents.json` file!



---





