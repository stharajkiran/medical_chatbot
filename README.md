# Build a medical chatbot using RAG

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/stharajkiran/medical_chatbot.git
```
### STEP 01- Install the requirements


### Install the packages and create virtual env

(install uv first)

Run
```bash
uv sync
```

This installs all the packages into the virtual environment. <br>
Activate the venv.



### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Makefile is provided. First activate the virtual env and then run
```bash
make start
```

(make should be installed first)


### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone
- make
- uv



# AWS-CICD-Deployment-with-Github-Actions

## 1. cicd.yaml used for github actions 

## 2. Use AWS EC2 instance for virtual power

## 3 Use ECR to store docker image