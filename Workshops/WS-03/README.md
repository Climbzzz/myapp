# DBAS 3200 Workshop 03 - Dockerized Django Application

## 1. Application Purpose and Architecture

This project demonstrates a Dockerized Django web application connected to a PostgreSQL database using Docker Compose.

Architecture:

- Django web application (`web`)
- PostgreSQL database (`db`)
- Docker Compose orchestration
- Persistent PostgreSQL volume (`pgdata`)

---

## 2. OS and Development Tooling

Operating System:
- Ubuntu (WSL 2)

Development Tools:
- Docker Desktop
- Docker Compose
- Python 3.12
- Django
- PostgreSQL 16
- Git
- VS Code
- GNU Make

---

## 3. Dockerfile and Compose Services

### Dockerfile

The Dockerfile:

- Uses the Python 3.12 slim image
- Installs project dependencies
- Copies application files
- Exposes port 8000
- Starts the Django development server

### Compose Services

#### db

PostgreSQL database service.

#### web

Django application service.

---

## 4. .env versus .env.example

### .env.example

Contains example configuration values and is committed to Git.

Example:

```env
POSTGRES_DB=myapp_db
POSTGRES_USER=myapp_user
POSTGRES_PASSWORD=replace-with-a-local-password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### .env

Contains actual local configuration values and is ignored by Git.

---

## 5. Build and Run Instructions

Build containers:

```bash
make build
```

Start services:

```bash
make up
```

Check services:

```bash
make ps
```

Stop services:

```bash
make down
```

Application URL:

http://localhost:8000

---

## 6. Migration Instructions

Create migrations:

```bash
make makemigrations
```

Apply migrations:

```bash
make migrate
```

Verify project:

```bash
make check
```

---

## 7. Application URL

Local application:

http://localhost:8000

---

## 8. PostgreSQL Persistence

PostgreSQL data is stored using the named volume:

```yaml
pgdata
```

Data remains available after:

```bash
docker compose down
docker compose up -d
```

because the volume persists independently of the containers.

---

## 9. Makefile Reference

Build project:

```bash
make build
```

Start services:

```bash
make up
```

Stop services:

```bash
make down
```

View running services:

```bash
make ps
```

View logs:

```bash
make logs
```

Run Django checks:

```bash
make check
```

Apply migrations:

```bash
make migrate
```

Open Django shell:

```bash
make shell
```

Open PostgreSQL shell:

```bash
make dbshell
```

Create superuser:

```bash
make superuser
```

---

## 10. Troubleshooting Observations

During development several issues were encountered:

- Missing PostgreSQL password configuration.
- Docker container restart loops.
- Empty compose.yaml file.
- File ownership and permission issues created by Docker.
- Existing Django app name conflicts.
- Git branch divergence requiring synchronization with GitHub.

These issues were resolved through Docker log inspection, environment configuration updates, volume recreation, and Git troubleshooting commands.