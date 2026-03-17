# 🚀 AI Research Assistant

An AI-powered Research Assistant that provides intelligent, context-aware responses using LLMs, agent workflows, and memory.

---

## 📌 Features

- 🔍 LLM-based Question Answering  
- 🧠 Short-term Memory (last interactions)  
- ⚡ Agent-based architecture  
- 🌐 Interactive UI (Streamlit / Gradio)  
- 🔄 Extensible (LangGraph-ready design)  
- 🧪 Unit & Integration Testing  
- 📊 Logging, Retry & Exception Handling  


---

## ⚙️ Installation

```bash
git clone https://github.com/cheerlaminusri/AI-Research-Assistant.git
cd AI-Research-Assistant

python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Run Application

### Streamlit
```bash
streamlit run app.py
```

### Gradio
```bash
python app/gradio_app.py
```

---

## 🧠 Workflow

```
User Query
   ↓
Agent
   ↓
Memory Retrieval
   ↓
LLM Response
   ↓
Store Memory
   ↓
UI Output
```

---

## 🔁 Memory Example

```python
memory = []

def save_interaction(query, answer):
    memory.append({"query": query, "answer": answer})

def get_recent_memory():
    return memory[-5:]
```

---

## 🧪 Testing

```bash
pytest
```

---

## 📦 Tech Stack

- Python  
- LangGraph / LangChain  
- Streamlit   
- OpenAI APIs  
- Pytest  

---

## 🚀 Future Improvements

- RAG (Vector DB + Embeddings)  
- Multi-agent workflows  
- Tool integrations  
- Docker deployment  
- Cloud deployment  

---

## 👨‍💻 Author

Minusri Cheerla

---

## ⭐ Use Cases

- AI Research Assistant  
- Chatbot  
- GenAI demo project  
- Interview portfolio  

---

## 📜 License

MIT License