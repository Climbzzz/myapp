![alt text](NSCC-ITOS-Wordmark.png)

---
# DBAS 3200 — Data Driven Application Programming

## Workshop 0 — Development Environment & Tooling Setup

---

## 1. Workshop Details

| Field                     | Information                                          |
| ------------------------- | ---------------------------------------------------- |
| **Course Code**           | DBAS 3200                                            |
| **Course Name**           | Data Driven Application Programming                  |
| **Instructor**            | Davis Boudreau                                       |
| **Workshop**              | Workshop 0 — Development Environment & Tooling Setup |
| **Workshop Type**         | Tooling Readiness / Collaborative Applied Learning   |
| **Estimated Time**        | 4 hours in class + additional setup time if required |
| **Learning Outcomes**     | Outcomes 2, 6                                        |
| **Weight**                | 0% — Required/Formative                              |
| **Semester**              | Fall 2026                                            |
| **Reflection Submission** | Not Required                                         |

> **Workshop 0 is required but formative.** Reflection questions are included at the end of the workshop, but you are **not required to submit your answers to Brightspace for Workshop 0**.

---

# 2. Workshop Overview

## Purpose

Before we can develop data-driven applications, we need a reliable development environment.

In this workshop, you will configure and verify the tools that will become part of your normal DBAS 3200 development workflow:

**VS Code → Python → Virtual Environment → Django → Git/GitHub → Make → Docker → Docker Compose**

You will then build a small Django application twice conceptually:

1. first as a normal Python application using a local virtual environment; and
2. then as a containerized application using Docker.

The objective is not simply to install software. You should begin to understand **what each tool does, why we use it, and how the tools work together**.

## Why This Matters

A developer should be able to obtain a project, prepare the required environment, install its dependencies, run it, troubleshoot it, and reproduce the process on another system.

Throughout DBAS 3200, we will work toward a professional workflow:

**Clone → Configure → Build → Develop → Test → Commit → Integrate → Reproduce → Deploy**

Workshop 0 establishes the foundation for that workflow.

## Learning Objectives

By the end of this workshop, you should be able to:

1. Verify that your computer is ready for DBAS 3200 development.
2. Install and configure VS Code and the required development extensions.
3. Install and verify Python, Git, GitHub access, Docker, and Docker Compose.
4. Create and use a Python virtual environment.
5. Install Django into an isolated development environment.
6. Explain the difference between a Django **project** and a Django **app**.
7. Create and run a basic Django project.
8. Create a Django application, view, URL route, and template.
9. Initialize and maintain the project using Git.
10. Use `.gitignore`, `.dockerignore`, `requirements.txt`, and related project files appropriately.
11. use Make to simplify common development commands.
12. Build and run the sample Django application using Docker.
13. Verify that the development environment is ready for future DBAS 3200 workshops.

---

# 3. Learning Outcomes Addressed

### Outcome 2 — Create and manage a data connection

Workshop 0 establishes the development environment that will later be used to configure and manage application/database connections.

### Outcome 6 — Develop professionalism by receiving specifications, developing and deploying solutions in a project-managed context

Students establish a repeatable development workflow using source control, environment isolation, documentation, automation, and containers.

---

# 4. Before We Begin — Prior Knowledge Check

Before installing anything, discuss the following with your classmates and instructor.

1. What development tools have you used before?
2. Have you used Git from the command line?
3. Have you pushed a project to GitHub?
4. What is a Python virtual environment?
5. Why might two developers running the same Python program get different results?
6. What is the difference between a **virtual environment** and a **container**?
7. Have you used Docker or Docker Compose?
8. What do you think a `Dockerfile` does?
9. What problem does a `.gitignore` file solve?
10. What is the purpose of a `requirements.txt` file?
11. Have you used Make or another build/task automation tool?
12. Have you developed an application using Django or another web framework?

There is no expectation that everyone will have the same answers.

The purpose is to establish:

**What do we know? → How deeply do we understand it? → What do we need to learn?**

---

# 5. Concepts & Theory

Before beginning the technical work, make sure you understand the role of each component.

| Concept                           | What You Need to Understand                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------- |
| **VS Code**                       | Development environment used to edit, navigate, run, debug, and manage project files.        |
| **Python**                        | Programming runtime used by Django.                                                          |
| **pip**                           | Python package installer used to install project dependencies.                               |
| **Virtual Environment (`.venv`)** | Isolates Python packages for one project from the global Python installation.                |
| **Django**                        | Python web application framework.                                                            |
| **Django Project**                | Overall configuration and structure for a Django website/application environment.            |
| **Django App**                    | A functional component within a Django project.                                              |
| **Git**                           | Distributed source-control system that records project history.                              |
| **GitHub**                        | Remote collaboration and repository platform used with Git.                                  |
| **`.gitignore`**                  | Identifies files and directories that should not be tracked by Git.                          |
| **`requirements.txt`**            | Records Python dependencies needed to recreate the application's Python environment.         |
| **Docker**                        | Packages an application and its runtime dependencies into reproducible containers.           |
| **Dockerfile**                    | Instructions used to build a container image.                                                |
| **Docker Compose**                | Defines and coordinates one or more application services.                                    |
| **`.dockerignore`**               | Prevents unnecessary files from being included in a Docker build context.                    |
| **Make / Makefile**               | Provides consistent shortcuts for common development commands.                               |
| **Markdown**                      | Lightweight documentation format commonly used for README files and technical documentation. |
| **Mermaid**                       | Text-based diagramming syntax that can be embedded in Markdown documentation.                |

---

# 6. Presentation & Demonstration

Before beginning the workshop tasks, we will examine how the development environment fits together.

The instructor will demonstrate the relationship between:

**Developer**
↓
**VS Code**
↓
**Git Repository**
↓
**Python / `.venv`**
↓
**Django**
↓
**Docker**
↓
**Application Services**

We will also discuss an important distinction:

### Local Development Environment

```text
Windows
└── Python
    └── .venv
        └── Django
            └── Application
```

### Containerized Development Environment

```text
Windows
└── Docker Desktop / WSL 2
    └── Container
        └── Python
            └── Django
                └── Application
```

A virtual environment isolates **Python packages**.

A container isolates much more of the **application runtime environment**.

We will use both during the course because understanding both helps explain what Docker is actually solving.

---

# 7. Workshop Challenge — Discuss & Analyze

## Scenario

You have joined a development team working on a new data-driven application.

Before development begins, every team member needs a consistent set of tools and must be able to:

* obtain the project;
* open it in VS Code;
* create an isolated Python environment;
* install dependencies;
* run the Django application;
* track the project using Git;
* work with GitHub;
* build the application using Docker;
* run the application using Docker Compose;
* understand the project documentation; and
* reproduce the development environment on another computer.

## Before You Build

Discuss:

* Which tools belong on the developer's computer?
* Which dependencies belong inside the project?
* Which files should be tracked by Git?
* Which files should **not** be tracked?
* Should `.venv` be committed?
* Why do we need `requirements.txt` if we already have `.venv`?
* What problem will Docker solve that `.venv` does not?
* How can another developer determine how to run our application?
* How do we prove that our environment is working?

---

# 8. Workshop Tasks

## Task 1 — Workstation Readiness Check

### What

Determine whether your computer meets the basic requirements for the DBAS 3200 development environment.

### Why

Installing tools before verifying operating-system, virtualization, storage, and permission requirements can lead to difficult-to-diagnose problems later.

### How

Verify:

* Windows is current and supported.
* Hardware virtualization is enabled.
* WSL 2 is available and current.
* You have sufficient available storage.
* You can install the required development software.
* You can access the course CMS (Brightspace).
* You can access GitHub.
* You can open a terminal/PowerShell session.

Check WSL:

```powershell
wsl --version
```

If WSL is not installed:

```powershell
wsl --install
```

If WSL requires updating:

```powershell
wsl --update
```

A restart may be required.

### Checkpoint

You can successfully display WSL version information and have no unresolved virtualization or operating-system issues.

---

## Task 2 — Install and Configure Visual Studio Code

### What

Install or verify VS Code and configure the extensions required for the course.

### Why

VS Code will act as the primary workspace for source code, terminals, Git, Markdown documentation, diagrams, configuration files, and other project artifacts.

### How

Install or verify VS Code.

Open **Extensions** using:

```text
Ctrl + Shift + X
```

At minimum, prepare support for:

* Python
* Python environments
* Git/GitHub workflow
* Markdown
* Mermaid diagrams
* PDF viewing
* CSV viewing
* Docker/container files
* YAML
* GitHub integration

Your instructor may identify specific extensions to standardize the classroom environment.

Do not install extensions simply because they are popular. Understand what problem each extension solves.

### Checkpoint

Open VS Code and confirm that Python, Markdown, Mermaid, PDF/CSV viewing, Git/GitHub, and container-development capabilities are available.

---

## Task 3 — Install and Verify Python

### What

Install or verify a supported Python 3 installation.

### Why

Django is a Python framework. Your host Python installation will also allow us to understand local development before moving the application into a container.

### How

Open the VS Code terminal.

On Windows:

```powershell
py --version
```

Also try:

```powershell
python --version
```

Check pip:

```powershell
py -m pip --version
```

For this course environment, use **Python 3.12 or later**.

### Checkpoint

You can display your Python and pip versions from the VS Code terminal.

---

## Task 4 — Install and Configure Git

### What

Install Git and establish your basic developer identity.

### Why

Git will be part of the normal development workflow throughout DBAS 3200.

### How

Verify Git:

```bash
git --version
```

Configure your identity if required:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Verify:

```bash
git config --global --list
```

### Checkpoint

Git reports its version and your correct name/email configuration.

---

## Task 5 — Verify GitHub Access

### What

Confirm that you can authenticate with GitHub and work with course repositories.

### Why

Git is the source-control system. GitHub provides the remote repository and collaboration environment we will use throughout the course.

### How

Verify that you can:

1. Sign in to GitHub.
2. Access course repositories when provided.
3. Clone a repository.
4. Commit locally.
5. Push to a remote repository.

Your instructor will discuss the authentication method used for the course.

### Checkpoint

You can access GitHub and are ready to clone/push repositories.

---

## Task 6 — Install and Verify Docker Desktop

### What

Install Docker Desktop and verify Docker Engine and Docker Compose.

### Why

Containers will be part of our normal DBAS 3200 development workflow. They allow us to define reproducible application and database environments.

### How

Install Docker Desktop using the WSL 2 backend.

After installation, start Docker Desktop.

Verify:

```bash
docker --version
```

Verify Compose:

```bash
docker compose version
```

Run a basic container test:

```bash
docker run --rm hello-world
```

### What Just Happened?

When you ran `hello-world`, Docker:

1. received a request from the Docker client;
2. checked whether the image existed locally;
3. downloaded the image if required;
4. created a container from the image;
5. executed the container; and
6. displayed the container output.

This distinction will become important:

**Image → Container**

An image is a packaged definition.

A container is a running—or previously run—instance created from that image.

### Checkpoint

All three commands work:

```bash
docker --version
docker compose version
docker run --rm hello-world
```

---

## Task 7 — Prepare Make

### What

Ensure you have access to the `make` command.

### Why

A Makefile gives a project a simple and consistent interface for frequently used commands.

Instead of remembering long commands, developers can use commands such as:

```bash
make run
make test
make docker-up
```

### How

Verify:

```bash
make --version
```

If Make is not available directly in your Windows environment, your instructor will demonstrate the course-supported approach for using GNU Make, including the WSL environment where appropriate.

### Checkpoint

You have an identified and tested method for running `make`.

---

## Task 8 — Create the Workshop Project

### What

Create a clean project workspace.

### Why

A predictable project structure makes source control, environment management, documentation, and containerization easier.

### How

Create:

```text
dbas3200-workshop0
```

Open the folder in VS Code.

From a terminal:

```bash
mkdir dbas3200-workshop0
cd dbas3200-workshop0
code .
```

Initialize Git:

```bash
git init
```

Check:

```bash
git status
```

### Checkpoint

The project folder is open in VS Code and Git reports that it is a repository.

---

## Task 9 — Create a Python Virtual Environment

### What

Create an isolated Python environment named `.venv`.

### Why

Installing Django globally can create dependency conflicts between projects.

Each project should be able to maintain its own dependencies.

### How

Create the environment:

```powershell
py -m venv .venv
```

PowerShell activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

macOS/Linux/WSL:

```bash
source .venv/bin/activate
```

After activation, your terminal should indicate that `.venv` is active.

Verify:

```bash
python --version
python -m pip --version
```

In VS Code, confirm that the `.venv` Python interpreter is selected.

### Important

The `.venv` directory is **local development state**.

We do not share the `.venv` directory through Git.

We share the information required to **recreate it**.

### Checkpoint

VS Code and your terminal are using the Python interpreter inside `.venv`.

---

## Task 10 — Install Django

### What

Install Django into the virtual environment.

### Why

Django should belong to this project's dependency environment rather than being assumed to exist globally.

### How

With `.venv` active:

```bash
python -m pip install --upgrade pip
python -m pip install "Django>=6.1,<6.2"
```

Verify:

```bash
python -m django --version
```

Record the environment:

```bash
python -m pip freeze > requirements.txt
```

Inspect `requirements.txt`.

### Discuss

Why do we commit:

```text
requirements.txt
```

but not:

```text
.venv/
```

### Checkpoint

Django reports its version and `requirements.txt` exists.

---

## Task 11 — Create the Django Project

### What

Create the Django **project**.

### Why

The Django project contains the overall configuration for the website, including settings, URL configuration, and server interfaces.

### How

Run:

```bash
django-admin startproject config .
```

The period (`.`) matters.

It tells Django:

> Create the project in the **current directory**.

Your project should now resemble:

```text
dbas3200-workshop0/
├── .venv/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

### Understand the Files

`manage.py`
Command-line interface for managing this Django project.

`config/settings.py`
Project configuration.

`config/urls.py`
Top-level URL routing.

`config/asgi.py` and `config/wsgi.py`
Interfaces used when serving the Django application.

### Checkpoint

Run:

```bash
python manage.py check
```

Django should report no system-check issues.

---

## Task 12 — Apply the Initial Database Migrations

### What

Initialize Django's built-in database structures.

### Why

Django includes components such as authentication, sessions, and administration that require database tables.

For Workshop 0, Django's default SQLite database is sufficient.

### How

Run:

```bash
python manage.py migrate
```

Notice the new file:

```text
db.sqlite3
```

### Discuss

Why are we using SQLite now rather than PostgreSQL?

Workshop 0 is about understanding and validating the **development environment**.

Later workshops will deliberately introduce database connectivity, PostgreSQL, ORM configuration, migrations, and containerized database services when those concepts become the focus of the learning.

### Checkpoint

Migrations complete successfully.

---

## Task 13 — Run the Django Development Server

### What

Start Django's built-in development server.

### Why

Before building application functionality, we should prove that the framework and environment are working.

### How

Run:

```bash
python manage.py runserver
```

Open the local address displayed by Django in your browser.

You should see Django's default success page.

Stop the server with:

```text
Ctrl + C
```

### Checkpoint

The Django development server runs successfully and the default page loads.

---

## Task 14 — Create Your First Django App

### What

Create an application named `core`.

### Why

A Django **project** is the overall application environment.

A Django **app** is a component that performs a particular responsibility.

This distinction is fundamental to Django architecture.

### How

Run:

```bash
python manage.py startapp core
```

You should now have:

```text
core/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

Register the app in `config/settings.py`:

```python
INSTALLED_APPS = [
    # Django applications...
    "core",
]
```

### Checkpoint

Run:

```bash
python manage.py check
```

No configuration errors should be reported.

---

## Task 15 — Create a View

### What

Create a Django view that responds to a web request.

### Why

A browser sends an HTTP request.

Django must determine what Python code should handle that request and what response should be returned.

### How

Open:

```text
core/views.py
```

Add:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello from DBAS 3200!")
```

### Understand It

`request` represents the incoming HTTP request.

`home()` is our view function.

`HttpResponse()` creates the response returned to the browser.

But Django does not yet know **which URL should call this view**.

That is our next task.

---

## Task 16 — Connect the View to a URL

### What

Map the root URL to the `home` view.

### Why

Django's URL dispatcher connects a requested URL to application logic.

Conceptually:

```text
Browser Request
      ↓
URL Pattern
      ↓
View
      ↓
Response
      ↓
Browser
```

### How

Open:

```text
config/urls.py
```

Configure:

```python
from django.contrib import admin
from django.urls import path
from core.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
]
```

Run:

```bash
python manage.py runserver
```

Refresh the browser.

### Checkpoint

The browser displays:

```text
Hello from DBAS 3200!
```

---

## Task 17 — Move from a Simple Response to a Template

### What

Replace the plain text response with an HTML template.

### Why

Real applications separate presentation markup from Python application logic.

Instead of constructing HTML inside our Python code, the view can render a template.

### How

Create:

```text
templates/
└── home.html
```

In `config/settings.py`, locate `TEMPLATES` and configure:

```python
"DIRS": [BASE_DIR / "templates"],
```

Update `core/views.py`:

```python
from django.shortcuts import render


def home(request):
    context = {
        "course": "DBAS 3200",
        "message": "Development environment ready!"
    }

    return render(request, "home.html", context)
```

Create `templates/home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DBAS 3200 Workshop 0</title>
</head>
<body>
    <main>
        <h1>{{ course }}</h1>
        <p>{{ message }}</p>
    </main>
</body>
</html>
```

### What Is Happening?

The request now follows:

```text
Browser
   ↓
config/urls.py
   ↓
core.views.home()
   ↓
context data
   ↓
templates/home.html
   ↓
HTML Response
   ↓
Browser
```

### Checkpoint

Your browser renders the HTML page and displays the values passed from the Django view.

---

## Task 18 — Create `.gitignore`

### What

Tell Git which local files should not be tracked.

### Why

A repository should contain the files required to **recreate** the project—not every file generated on your computer.

### How

Create:

```text
.gitignore
```

Example:

```gitignore
# Python
__pycache__/
*.py[cod]
*.log

# Virtual environments
.venv/
venv/
env/

# Environment / secrets
.env
.env.*

# Django
db.sqlite3
media/
staticfiles/

# IDE / OS
.vscode/
.idea/
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.bak
*.swp
```

### Discuss

Why should these be ignored?

* `.venv/`
* `.env`
* `db.sqlite3`
* `__pycache__/`

### Checkpoint

Run:

```bash
git status
```

Confirm `.venv` is not listed as a set of files waiting to be committed.

---

## Task 19 — Add a README

### What

Document the project.

### Why

A repository should explain what the project is and how another developer can work with it.

### How

Create:

```text
README.md
```

Include:

````markdown
# DBAS 3200 — Workshop 0

## Purpose

Development environment and tooling verification for DBAS 3200.

## Local Setup

Create a virtual environment:

```text
py -m venv .venv
````

Activate the environment and install dependencies:

```text
python -m pip install -r requirements.txt
```

Apply migrations:

```text
python manage.py migrate
```

Run the application:

```text
python manage.py runserver
```

````

Preview your Markdown in VS Code.

Add a small Mermaid diagram:

```text
flowchart LR
    Browser --> Django
    Django --> View
    View --> Template
    Template --> Browser
````

Preview the diagram using your configured Markdown/Mermaid tooling.

### Checkpoint

Your README renders correctly and the Mermaid diagram can be viewed.

---

## Task 20 — Make Your First Git Commit

### What

Create the first meaningful snapshot of the project.

### Why

Git history should describe the development of the project.

### How

Review first:

```bash
git status
```

Stage:

```bash
git add .
```

Review again:

```bash
git status
```

Commit:

```bash
git commit -m "Initialize Django development environment"
```

Review:

```bash
git log --oneline
```

### Checkpoint

Your repository contains an initial commit and does not contain `.venv`.

---

## Task 21 — Create a Makefile

### What

Create shortcuts for common development tasks.

### Why

A Makefile provides a consistent project interface and reduces repetitive commands.

### How

Create:

```text
Makefile
```

Add:

```makefile
.PHONY: install run check migrate test docker-build docker-up docker-down

install:
	python -m pip install -r requirements.txt

run:
	python manage.py runserver

check:
	python manage.py check

migrate:
	python manage.py migrate

test:
	python manage.py test

docker-build:
	docker compose build

docker-up:
	docker compose up

docker-down:
	docker compose down
```

> Makefile command indentation must use **tabs**, not spaces.

Try:

```bash
make check
```

and:

```bash
make run
```

### Checkpoint

At least the `check` and `run` targets execute successfully using the course-supported Make environment.

---

## Task 22 — Prepare the Application for Docker

### What

Create a Docker image definition for the Django application.

### Why

The `.venv` approach isolates Python packages, but it still depends on Python and other tooling installed on the host computer.

Docker allows us to define the application's runtime environment as part of the project.

### How

Create:

```text
Dockerfile
```

Add:

```dockerfile
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Discuss

Compare:

```text
Host Python + .venv
```

with:

```text
Docker Image + Container
```

What dependencies move into the container?

What still remains on the host?

---

## Task 23 — Create `.dockerignore`

### What

Control which files Docker sends into the build context.

### Why

The container does not need our local virtual environment, Git history, temporary files, or other local development artifacts.

### How

Create:

```text
.dockerignore
```

Add:

```dockerignore
.git
.gitignore
.venv
__pycache__
*.pyc
*.pyo
*.log
.env
db.sqlite3
.vscode
.idea
README.md
```

### Checkpoint

Review the difference between:

```text
.gitignore
```

and:

```text
.dockerignore
```

They solve related but different problems.

---

## Task 24 — Create Docker Compose Configuration

### What

Define the Django application as a Docker Compose service.

### Why

Compose gives us a consistent way to define, start, stop, and later connect multiple services.

Today we have one service.

Later we may have:

```text
web
database
cache
API
worker
```

### How

Create:

```text
compose.yaml
```

Add:

```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```

### Checkpoint

Validate:

```bash
docker compose config
```

Docker Compose should successfully parse the configuration.

---

## Task 25 — Build the Docker Image

### What

Build the Django application image.

### Why

The image packages the Python runtime, Django dependencies, project files, and startup configuration.

### How

Run:

```bash
docker compose build
```

Or:

```bash
make docker-build
```

Watch the build process.

Identify where Docker:

1. obtains Python;
2. creates the working directory;
3. copies `requirements.txt`;
4. installs Django;
5. copies the application; and
6. defines the startup command.

### Checkpoint

Run:

```bash
docker images
```

Confirm that the project image exists.

---

## Task 26 — Run Django in Docker

### What

Run the application from the container rather than your host `.venv`.

### Why

This demonstrates the central idea of reproducibility.

The application is now running using the Python and Django environment defined by the Docker image.

### How

Run:

```bash
docker compose up
```

Or:

```bash
make docker-up
```

Visit the application in your browser.

### Think About It

The page looks the same.

But is it running in the same environment?

No.

Previously:

```text
Windows → .venv → Python → Django
```

Now:

```text
Windows → Docker → Linux Container → Python → Django
```

### Checkpoint

Your Django page loads successfully while running from Docker.

---

## Task 27 — Inspect and Troubleshoot the Container

### What

Observe the running application rather than treating Docker as a black box.

### Why

Professional developers must be able to determine what is running and diagnose problems.

### How

In another terminal:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Follow logs:

```bash
docker compose logs -f
```

Stop:

```bash
docker compose down
```

### Troubleshooting Questions

What happens if:

* port 8000 is already in use?
* `requirements.txt` is missing?
* the Dockerfile contains a syntax error?
* the Django server binds only to `127.0.0.1` inside the container?
* you change Python dependencies but do not rebuild the image?

### Checkpoint

You can start, inspect, view logs for, and stop the application.

---

## Task 28 — Update the Makefile

### What

Use Make as a consistent interface for both local and Docker workflows.

### Why

A developer should not need to memorize every underlying command before being productive in a project.

### How

Your final Makefile should provide useful commands such as:

```makefile
.PHONY: install run check migrate test docker-build docker-up docker-down docker-logs

install:
	python -m pip install -r requirements.txt

run:
	python manage.py runserver

check:
	python manage.py check

migrate:
	python manage.py migrate

test:
	python manage.py test

docker-build:
	docker compose build

docker-up:
	docker compose up

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f
```

Run several targets and identify the underlying commands they execute.

### Checkpoint

You understand that Make does not replace Docker, Django, or Python.

It provides a **consistent interface to those tools**.

---

## Task 29 — Final Project Structure

Your completed Workshop 0 project should resemble:

```text
dbas3200-workshop0/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Makefile
├── README.md
├── compose.yaml
├── manage.py
├── requirements.txt
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── templates/
    └── home.html
```

Locally you will also have:

```text
.venv/
db.sqlite3
```

but these should not be part of the Git repository.

---

## Task 30 — Final Tooling Verification

Before considering Workshop 0 complete, verify each item.

| Tool / Capability       | Verification                        |
| ----------------------- | ----------------------------------- |
| **VS Code**             | Opens project successfully          |
| **Python**              | `python --version`                  |
| **pip**                 | `python -m pip --version`           |
| **Virtual Environment** | `.venv` created and selected        |
| **Django**              | `python -m django --version`        |
| **Django Check**        | `python manage.py check`            |
| **Git**                 | `git --version`                     |
| **Git Repository**      | `git status`                        |
| **GitHub**              | Account/repository access confirmed |
| **Docker**              | `docker --version`                  |
| **Docker Compose**      | `docker compose version`            |
| **Container Test**      | `docker run --rm hello-world`       |
| **Make**                | `make --version`                    |
| **Markdown**            | README preview works                |
| **Mermaid**             | Diagram preview works               |
| **PDF**                 | PDF viewing available               |
| **CSV**                 | CSV viewing available               |
| **Local Django**        | Application runs from `.venv`       |
| **Docker Django**       | Application runs through Compose    |

---

# 9. Collaborative Investigation & Troubleshooting

Workshop 0 is intentionally collaborative.

You are encouraged to help classmates identify:

* missing prerequisites;
* PATH problems;
* incorrect Python interpreters;
* virtual environment problems;
* Git configuration issues;
* WSL problems;
* Docker startup problems;
* virtualization issues;
* port conflicts;
* Docker build errors;
* VS Code extension/configuration problems.

When helping another student, avoid simply taking over their keyboard and fixing the problem.

Instead:

1. identify the symptom;
2. ask what they expected;
3. inspect the evidence;
4. form a hypothesis;
5. test the hypothesis;
6. explain the solution.

> **Collaborate on the problem. Understand your own solution.**

---

# 10. Workshop Checkpoints & Evidence

| Checkpoint                             | Evidence                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **1 — Workstation Readiness**          | Python, Git, GitHub, VS Code, Docker/Compose, WSL and Make are available or an approved remediation plan is established. |
| **2 — Local Development**              | `.venv` created, Django installed, sample project/app created and application runs locally.                              |
| **3 — Professional Project Structure** | Git repository, `.gitignore`, `requirements.txt`, README and Makefile are present and understood.                        |
| **4 — Container Workflow**             | Dockerfile, `.dockerignore`, Compose configuration and containerized Django application operate successfully.            |
| **5 — Documentation**                  | Markdown and Mermaid preview capabilities verified.                                                                      |
| **6 — Troubleshooting**                | Student can identify and explain at least one setup issue encountered or investigated.                                   |

---

# 11. Workshop Debrief

As a class, discuss:

* Which installation or configuration problems were most common?
* Which tools were already familiar?
* Which tools were new?
* What is the difference between `.venv` and Docker?
* Why do we need both `.gitignore` and `.dockerignore`?
* Why is `requirements.txt` important?
* What did Make simplify?
* What is the difference between a Django project and a Django app?
* What path does a request follow from the browser to a Django view?
* What evidence would convince you that another developer could reproduce your environment?
* What should we improve before beginning Workshop 1?

---

# 12. Reflection & Takeaways

Consider the following questions after completing Workshop 0.

### 1. Prior Knowledge

Which of the tools used today were you already comfortable with, and which were new to you?

### 2. Environment Isolation

What is the difference between using a Python virtual environment and running the application in Docker?

### 3. Django

Explain the difference between a Django **project** and a Django **app** in your own words.

### 4. Reproducibility

Why should `.venv` not be committed to Git? What files allow another developer to recreate the environment instead?

### 5. Tool Integration

How do Git, GitHub, VS Code, Python, Django, Make, and Docker contribute different responsibilities to the development workflow?

### 6. Troubleshooting

What was the most significant setup or configuration problem you encountered? How did you diagnose it?

### 7. Readiness

What part of your development environment do you still need to practise or improve before beginning the semester application?

> **Workshop 0 Reflection:** You should think about and discuss these questions, but **you do not submit your answers to Brightspace for Workshop 0**.

---

# 13. Workshop Evaluation

Workshop 0 uses the normal workshop criteria as a **formative readiness check**.

| Code  | Criterion                        | Evidence                                                                                                  |
| ----- | -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **A** | **Attendance**                   | Present for the scheduled workshop and tooling activities.                                                |
| **P** | **Participation**                | Participates in discussion, setup, peer troubleshooting, demonstrations, and workshop activities.         |
| **T** | **Task Progress**                | Makes meaningful progress toward a functioning DBAS 3200 development environment.                         |
| **F** | **Focus & Professional Conduct** | Uses workshop time effectively and demonstrates appropriate collaborative and professional behaviour.     |
| **R** | **Reflection / Exit Evidence**   | Reflection questions are considered and discussed; Brightspace submission is not required for Workshop 0. |

**Workshop Weight: 0% — Required/Formative**

The purpose of Workshop 0 is to establish readiness and identify problems early—not to penalize students whose machines require additional troubleshooting.

---

# 14. Submission Guidelines

There is **no formal file upload required for Workshop 0**.

There is also **no Brightspace reflection submission required for Workshop 0**.

Students are expected to:

* complete the tooling-readiness activities;
* maintain the Workshop 0 project locally;
* use Git/GitHub as directed by the instructor;
* resolve outstanding environment issues as soon as possible; and
* arrive at the next development workshop with a functional course environment.

Your instructor may ask you to demonstrate specific checkpoints during the workshop.

---

# 15. Resources & Equipment

## Required / Recommended Software

* Visual Studio Code
* Python 3.12+
* Git
* GitHub account/access
* Docker Desktop
* Docker Compose
* WSL 2 on Windows
* GNU Make or the course-supported Make environment
* Modern web browser

## VS Code Capabilities

Your VS Code environment should support:

* Python development
* Python virtual environments
* Git/GitHub
* Docker/container files
* Markdown preview
* Mermaid diagrams
* PDF viewing
* CSV viewing
* YAML
* integrated terminal use

## Course Resources

* Brightspace
* Course GitHub repositories
* Instructor demonstrations
* Workshop examples
* Course documentation

## Documentation

Use official documentation for:

* Python
* Django
* Git
* GitHub
* Visual Studio Code
* Docker
* Docker Compose
* GNU Make

---

# Workshop 0 Learning Journey

**Prior Knowledge**
↓
**Verify the Workstation**
↓
**Install & Configure Tools**
↓
**Create `.venv`**
↓
**Install Django**
↓
**Build a Django Project**
↓
**Create a Django App**
↓
**Understand URL → View → Template**
↓
**Establish Git & Project Hygiene**
↓
**Automate with Make**
↓
**Containerize with Docker**
↓
**Build & Run with Compose**
↓
**Test & Troubleshoot**
↓
**Debrief**
↓
**Reflect**
↓
**Ready for DBAS 3200**

---

## Workshop 0 Completion Goal

At the end of this workshop, the most important result is not the sample webpage.

The important result is that you can explain and demonstrate the development path:

**VS Code → Git/GitHub → Python → `.venv` → Django → Make → Docker → Compose**

You now have the development foundation that we will build on throughout DBAS 3200.

The next stages of the course will extend this environment into **database connectivity, PostgreSQL, data-access layers, Django ORM, querying, CRUD, validation, transactions, application integration, and reproducible deployment**.
