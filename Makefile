
# install the dependencies
install:
	@echo "Installing dependencies..."
	uv sync

# Store the embeddings in the vector database
store:
	@echo "Setting up the vector storage..."
	python store_index.py

# Run the Flask app
run:
	@echo "Run the flask app..."
	python app.py

# Build Docker image
build:
	@echo "Creating Docker image..."
	docker build -t medical_chatbot .

# Run Flask app locally
docker-run:
	@echo "Running Flask app in Docker..."
	docker run --env-file .env -p 8080:8080 medical_chatbot

# Runs both the vector database setup and the Flask app
start:
	make store
	make run


