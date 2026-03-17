# 🚀 Multi-Tool RAG AI Research Assistant with Cross-Encoder Reranking

An advanced AI research assistant that combines **Retrieval-Augmented Generation (RAG)** with **multi-tool agents** to deliver accurate, context-aware answers from both web and document sources.

This system enhances traditional RAG pipelines by introducing a **cross-encoder reranking layer**, significantly improving retrieval relevance and reducing hallucinations in LLM responses.

---

## 🔥 Key Highlights

- 🔍 Hybrid Retrieval: Combines **vector search (FAISS)** with **cross-encoder reranking**
- 🌐 Multi-Tool Agent: Supports **web search + document retrieval**
- 🧠 Context-Aware Responses using **LLMs**
- ⚡ Optimized for **accuracy vs latency trade-off**
- 💬 Interactive UI with **Streamlit**

---

## ⚙️ Installation

```bash
git clone https://github.com/cheerlaminusri/Multi-tool-rag-ai-research-assistant.git
cd Multi-tool-rag-ai-research-assistant

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