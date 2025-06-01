# 🧠 RAG Chatbot (LangChain + Flask + OpenAI)

This is a minimalist **Retrieval-Augmented Generation (RAG)** chatbot I built from scratch using:
- `LangChain`
- `OpenAI`
- `FAISS` for vector search
- `Flask` for the API interface
- Dockerized for smooth deployment anywhere (incl. AWS)

## 🔧 How It Works
1. Load custom knowledge from `/data/context.txt`
2. Embed with `OpenAIEmbeddings`
3. Store in in-memory vector DB (FAISS)
4. Accept user question → retrieve → pass to OpenAI → respond.

## 🚀 Run Locally
```bash
git clone https://github.com/YOUR_GITHUB/rag-chatbot.git
cd rag-chatbot
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
python app/main.py
```

## 📦 Docker Build & Run
```bash
docker build -t rag-bot .
docker run -p 5000:5000 --env OPENAI_API_KEY=your_key_here rag-bot
```

## ✍️ Built By
A passionate AI Engineer skilled in LangChain, Prompt Engineering, TensorFlow, Docker & Cloud.
