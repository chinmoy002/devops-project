# 🚀 DevOps Project — Flask CI/CD with Docker

A hands-on DevOps portfolio project demonstrating the workflow of developing, testing, containerizing, and automatically deploying a Flask application using GitHub Actions, Docker, and Docker Compose.

The project runs on a self-hosted CentOS Stream VM and is being progressively expanded toward a production-oriented DevOps workflow.

---

## 🏗️ Architecture

```text
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Test Job
    │     ├── Checkout repository
    │     ├── Python 3.12
    │     ├── Install dependencies
    │     └── Run pytest
    │
    ▼
Self-Hosted GitHub Actions Runner
    │
    ▼
CentOS Stream VM
    │
    ▼
/opt/devops-project
    │
    ▼
Docker Compose
    │
    ▼
Flask Container
    │
    ├── Port 5000
    ├── APP_VERSION
    └── Persistent Docker Volume
    │
    ▼
/health
    │
    ▼
Deployment Health Check
```

---

## 🛠️ Technology Stack

- Python
- Flask
- pytest
- Linux / CentOS Stream
- Git
- GitHub
- GitHub Actions
- Self-Hosted GitHub Actions Runner
- Docker
- Docker Compose
- systemd
- Oracle VirtualBox

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch triggers the GitHub Actions workflow.

### Continuous Integration

GitHub Actions:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs application dependencies
4. Installs development/test dependencies
5. Runs the pytest test suite

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ▼
Python Environment
   │
   ▼
Dependencies Installed
   │
   ▼
pytest
   │
   ▼
Tests Passed
```

### Continuous Deployment

After the tests pass, the deployment job runs on the self-hosted CentOS Stream runner.

The deployment process:

1. Updates `/opt/devops-project`
2. Stops the previous host-based deployment if required
3. Starts the Docker Compose deployment
4. Rebuilds the application when required
5. Performs an application health check
6. Reports deployment success or failure

```text
Tests Passed
     │
     ▼
Self-Hosted Runner
     │
     ▼
/opt/devops-project
     │
     ▼
Docker Compose
     │
     ▼
Flask Container
     │
     ▼
GET /health
     │
     ▼
OK
```

---

## 🐳 Docker

The Flask application is containerized using a custom `Dockerfile`.

The Docker image:

- Uses Python 3.12 slim
- Installs application dependencies
- Copies the Flask application
- Exposes port 5000
- Runs the Flask application

### Build the image

```bash
docker build -t devops-flask-app .
```

### Run the container

```bash
docker run -d \
  --name devops-flask-app \
  -p 5000:5000 \
  devops-flask-app
```

---

## 🧩 Docker Compose

Docker Compose is used to define and manage the application container.

The current Compose configuration provides:

- Application service
- Port mapping
- Environment variables
- Persistent Docker volume
- Automatic restart
- Compose-managed networking

### Current Compose configuration

```yaml
services:
  app:
    build: .
    container_name: devops-flask-compose
    ports:
      - "5000:5000"
    environment:
      APP_VERSION: "2.0"
    volumes:
      - app-data:/data
    restart: unless-stopped

volumes:
  app-data:
```

### Start the application

```bash
docker compose up -d --build
```

### Stop the application

```bash
docker compose down
```

### Check the running services

```bash
docker compose ps
```

---

## 💾 Persistent Storage

Docker Compose manages a named volume:

```text
app-data
```

which is mounted inside the Flask container:

```text
/data
```

The volume allows data stored in `/data` to survive container recreation.

The persistence behavior was tested by:

1. Creating data inside the container
2. Removing the container
3. Recreating the container
4. Verifying that the data remained

---

## 🌐 Docker Networking

Docker Compose automatically creates a project network for its services.

During development, container-to-container communication was tested using Docker's internal DNS and service names.

A temporary Nginx container was used to verify:

- Compose networking
- Container-to-container communication
- Docker DNS
- Service-name resolution
- Health checks
- `depends_on`

The temporary Nginx service was removed from the final project configuration after testing.

---

## ❤️ Application Health Check

The Flask application provides a dedicated health endpoint:

```text
GET /health
```

The endpoint returns:

```text
OK
```

The CI/CD deployment uses this endpoint to verify that the newly deployed application is responding correctly.

Test it manually:

```bash
curl http://localhost:5000/health
```

Expected output:

```text
OK
```

---

## ⚙️ Environment Configuration

The Flask application reads its version from an environment variable:

```python
os.getenv("APP_VERSION", "unknown")
```

Docker Compose provides the value:

```yaml
environment:
  APP_VERSION: "2.0"
```

This allows application configuration to be changed without modifying the application source code.

The running container can be inspected with:

```bash
docker compose exec app printenv APP_VERSION
```

Expected output:

```text
2.0
```

---

## 🧪 Automated Testing

The project uses `pytest` for automated testing.

Run the tests locally:

```bash
python -m pytest
```

The same test suite is executed by GitHub Actions before deployment.

A failed test prevents the deployment job from proceeding.

---

## 📁 Project Structure

```text
devops-project/
│
├── app/
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── runner-test.yml
│
├── Dockerfile
├── .dockerignore
├── compose.yaml
├── requirements.txt
├── requirements-dev.txt
└── .gitignore
```

---

## 🔐 Development and Deployment Directories

The project uses two separate working directories on the CentOS VM.

### Development Directory

```text
/home/chinmoy/devops-project
```

This is the development copy where changes are made, committed, and pushed to GitHub.

### Deployment Directory

```text
/opt/devops-project
```

This is the production-like deployment copy updated by the self-hosted GitHub Actions runner.

The overall flow is:

```text
/home/chinmoy/devops-project
          │
          │ git push
          ▼
       GitHub
          │
          │ GitHub Actions
          ▼
/opt/devops-project
          │
          ▼
    Docker Compose
          │
          ▼
    Flask Container
```

---

## 🚀 Running the Project Locally

Clone the repository:

```bash
git clone <repository-url>
cd devops-project
```

Start the application:

```bash
docker compose up -d --build
```

Check the service:

```bash
docker compose ps
```

Test the health endpoint:

```bash
curl http://localhost:5000/health
```

Expected:

```text
OK
```

Open the application:

```text
http://localhost:5000
```

---

## 📚 DevOps Roadmap

### Completed

- [x] Linux & Server Administration
- [x] Git & GitHub
- [x] CI/CD with GitHub Actions
- [x] Docker
- [x] Docker Compose

### Planned

- [ ] Terraform
- [ ] Ansible
- [ ] Kubernetes
- [ ] Monitoring & Logging
- [ ] Advanced CI/CD
- [ ] Production-oriented deployment practices

---

## 🎯 Project Goals

This project is being developed as a practical DevOps portfolio project.

The focus is on hands-on implementation of:

- Linux administration
- Version control
- CI/CD automation
- Containerization
- Container orchestration
- Infrastructure as Code
- Configuration management
- Kubernetes
- Monitoring and logging

The project will progressively evolve from a simple Flask application into a more production-oriented DevOps deployment.

---

## 👨‍💻 Author

**Chinmoy Pagar**

Electrical Engineering → DevOps / Cloud / Linux
