\# DevOps Cloud Project



A simple Flask web application built as part of a DevOps \& Cloud Engineering internship project. This app will be containerized with Docker and deployed to the cloud using CI/CD.



\## Tech Stack

\- Python 3.14

\- Flask



\## Setup Instructions



1\. Clone this repository

git clone https://github.com/Olalekan-hub/devops-cloud-project.git

cd devops-cloud-project



2\. Create and activate a virtual environment

python -m venv venv

venv\\Scripts\\activate





3\. Install dependencies

pip install flask





4\. Run the app
python app.py





5\. Visit `http://127.0.0.1:5000` in your browser




## Running with Docker

1. Build the Docker image
docker build -t devops-project .


2. Run the container
docker run -p 5000:5000 devops-project


3. Visit `http://127.0.0.1:5000` in your browser

## Screenshots
See the `screenshots/` folder for images of the app running inside Docker.




## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment. On every push to `main`:

1. CI (build-and-test): Installs dependencies, runs flake8 for code quality checks, and verifies the app imports without errors.
2. CD (build-and-deploy): If CI passes, builds a Docker image, pushes it to Azure Container Registry, and restarts the Azure Web App to pull the new image.

**Live application:** https://devops-project-webapp123.azurewebsites.net

Workflow file: `.github/workflows/ci-cd.yml`

See `screenshots/` for a successful pipeline run.



