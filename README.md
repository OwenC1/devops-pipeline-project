# TaskFlow – DevOps CI/CD Pipeline

## Project Overview

TaskFlow is a simple task management web application developed using Python and FastAPI. Users can view and add tasks through a web interface.

The purpose of this project is to demonstrate how DevOps tools and practices can be used to automate software testing, security checks, containerisation and deployment to AWS.

## Technologies Used

| Tool | Purpose |
|---|---|
| Python / FastAPI | Web application and REST API |
| Git / GitHub | Source code management and pull requests |
| GitHub Actions | Automated CI/CD pipelines |
| Pytest | Automated application testing |
| Ruff | Python code quality checks |
| Bandit | Python security analysis |
| Trivy | Docker image vulnerability scanning |
| Docker / Docker Compose | Containerisation and local services |
| AWS CloudFormation | Infrastructure as Code |
| AWS EC2 / ECR | Application hosting and Docker image storage |
| Prometheus / Grafana | Application monitoring and visualisation |

## CI/CD Pipeline

The pipeline is managed using GitHub Actions and runs automatically when changes are pushed or pull requests are created.

The continuous integration (CI) pipeline performs automated tests, code quality checks, security scanning and Docker image builds.

Once changes are merged into the main branch and CI succeeds, the continuous deployment (CD) pipeline builds and pushes the Docker image to Amazon ECR and deploys the updated application to an AWS EC2 instance.

CloudFormation is used to define the AWS infrastructure, while GitHub OIDC provides authentication without storing long-term AWS access keys.

## Running the Application Locally

The application can be started using Docker Compose.

```bash
docker compose up --build -d
```

Once the containers are running, the following services are available:

- TaskFlow application: http://localhost:8000
- API health check: http://localhost:8000/health
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

Stop the containers using:

```bash
docker compose down
```

## Monitoring and Logging

TaskFlow exposes application metrics through a `/metrics` endpoint. Prometheus collects these metrics, and Grafana displays information such as total HTTP requests, request rates and average response times.

The monitoring services run locally using Docker Compose. Application logs can also be viewed through Docker.

## Project Summary

This project demonstrates a CI/CD workflow from source code changes through automated testing and security checks to deployment on AWS. It also demonstrates how monitoring tools can provide visibility into application performance.

The pipeline was developed incrementally, with improvements made through testing, troubleshooting and pull requests.