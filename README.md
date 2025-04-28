## CodeBot: AI-Powered Python Code Assistant

CodeBot is a lightweight Flask-based web application designed to assist users in generating Python code snippets based on natural language prompts.
It interacts with OpenAI's GPT-3.5 Turbo model to transform user-provided descriptions into functional Python code, accompanied by a meaningful title.

## 📖 Project Overview

    Input: A natural language prompt (e.g., "Create a function to calculate Fibonacci numbers")

    Process: Send the prompt to OpenAI's GPT-3.5 Turbo model

    Output: Display the generated Python code along with a descriptive title

The goal is to demonstrate a simple AI-assisted development workflow through a clean API and minimalistic web interface.

## 🛠️ Tech Stack

    Backend: Python (Flask)

    Frontend: HTML ( inside app.py)

    Containerization: Docker

    Orchestration: Kubernetes (Minikube)

    External API: OpenAI GPT-3.5 Turbo Model

## 🚀 Local Development Setup

Follow these steps to set up and run the application locally:
### 1. Clone the Repository

git clone https://github.com/munevvernure/CodeBot-PythonAssistant.git

cd CodeBot-PythonAssistant

### 2. Create and Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate       # For Linux/macOS

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Configure Environment Variables

Create a .env file in the project root and add your OpenAI API Key:

OPENAI_API_KEY=your_openai_api_key_here

### 5. Run the Flask Application

python app.py

Visit http://127.0.0.1:5000 in your browser to access the application.

## 📦 Docker & Kubernetes Deployment

This project can be deployed inside a containerized environment and orchestrated using Kubernetes with Minikube.
### 1. Build and Push the Docker Image

docker build -t munevvernure/codebotapp:latest .

docker push munevvernure/codebotapp:latest

### 2. Start Minikube

minikube start

### 3. Deploy the Application to Kubernetes

kubectl apply -f deployment.yaml

### 4. Expose the Service

kubectl expose deployment codebotapp --type=NodePort --port=5000

### 5. Access the Service

Retrieve the URL to access the running service:

minikube service codebotapp --url

Open the printed URL in your browser.

## 🌐 Accessing the Application via Minikube

After deploying the application and exposing the service, you can access it using the Node IP and NodePort provided by Minikube.

For example, if your Minikube IP is 192.168.49.2 and the service is exposed on port 30007, you can open the application by visiting:

http://192.168.49.2:30007

    Note: Your Minikube IP and service port may vary depending on your local setup.
    You can always retrieve them by running:

    minikube ip
    kubectl get svc



## 📝 Important Notes

    Authentication: A valid OpenAI API key is required.

    Model Used: This project uses the OpenAI GPT-3.5 Turbo model.

    Containerization: The application includes a production-ready Dockerfile.

    Deployment: The app is deployed using a simple Kubernetes Deployment (deployment.yaml).

## 📚 Repository Contents
### File/Folder	Description
app.py	Main Flask application (includes HTML rendering)
Dockerfile	Docker image configuration
deployment.yaml	Kubernetes deployment manifest
requirements.txt	Python package requirements
