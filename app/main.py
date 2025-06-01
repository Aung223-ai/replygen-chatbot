# main.py
# Flask-based simple RAG chatbot using LangChain & OpenAI
from flask import Flask, request, jsonify
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

app = Flask(__name__)

# endpoint to ask questions
@app.route("/ask", methods=["POST"])
def ask():
    payload = request.get_json()
    question = payload.get("question", "").strip()
    if not question:
        return jsonify({"error": "No question provided."}), 400

    try:
        # load local context
        loader = TextLoader("data/context.txt")
        documents = loader.load()

        # embed and store in vector db (in-memory FAISS)
        vectordb = FAISS.from_documents(documents, OpenAIEmbeddings())

        # setup QA chain with retriever
        qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(), retriever=vectordb.as_retriever()
        )

        # query and return result
        answer = qa_chain.run(question)
        return jsonify({"question": question, "answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
