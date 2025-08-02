from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


load_dotenv()
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

# get embedding model
embedding_model = download_embeddings()
index_name = "medical-chatbot"

# Load the embeddings from pine cone database
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding_model
)

# LLM
chatModel = ChatOpenAI(model="gpt-4o")
# Retriever for findings docs similar to input query
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

# Prompt templete
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain) # retriever was built above in indices
 



# Flask part
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET","POST"])
def chat():
    input = request.form["msg"]
    print("input")
    response = rag_chain.invoke({"input": input})
    print("Response : ", response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug= True)