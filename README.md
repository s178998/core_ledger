# Core Ledger

**Core Ledger** is a lightweight Python-based ledger and user entry system.  
It supports both a **CLI interface** and a **web frontend with FastAPI backend**. Both interfaces share the same database and services, allowing seamless integration between command-line operations and web-based registration.

---

## Table of Contents

- [Overview](#overview)  
- [Phase 1: CLI](#phase-1-cli)  
- [Phase 2: Web Frontend + API](#phase-2-web-frontend--api)  
- [Requirements](#requirements)  
- [Setup](#setup)  
- [Usage](#usage)  
- [Running Tests](#running-tests)  
- [Database](#database)  
- [Project Structure](#project-structure)  

---

## Overview

Core Ledger provides a modular service architecture for creating, querying, and managing user entries.  
Phase 1 focused on **CLI-based entry management**, while Phase 2 extends the project with a **web frontend and REST API**, building directly on the services implemented in Phase 1.  

> Everything in Phase 2 relies on the same database and service layer from Phase 1, so CLI and web operations are fully compatible.

---

## Phase 1: CLI

### Features
- Add new users via CLI  
- Query all users or by ID  
- Delete all entries (for testing or administrative purposes)  
- Safe database sessions to prevent locks  
- Automated testing for core functionality  

### CLI Usage
Run the CLI:

```bash
python3 -m backend.cli.main
```

Available actions:

- Add a new user entry
- Query users
- Delete entries

## Phase 2: Web Frontend + API

Phase 2 builds on Phase 1, adding:

Features

 - FastAPI backend with endpoints:
 - POST /users/ → create user
 - GET /users/ → list all users
 - GET /users/{id} → retrieve a single user
 - DELETE /users/?confirm=True → delete all users

Web frontend (frontend/index.html) for registration
Dynamic form validation, success/error messages, responsive design
CORS-enabled backend for frontend communication
Shared database and services with Phase 1
Safe session handling to avoid SQLite database lock errors

## Frontend Usage

1. Start FastAPI backend:
``` bash
uvicorn main:app --reload
```

2. Serve the frontend (optional):
``` bash
cd frontend
python -m http.server 5500
```

Open in browser:
``` 
http://127.0.0.1:5500/frontend/user.html
```

## Submit entries; they are stored in the same database used by the CLI.

Phase 2 fully integrates with Phase 1: any user added via CLI is immediately visible through the web frontend/API, and vice versa.

## Requirements
- Python 3.10+
- pip
- SQLAlchemy
- FastAPI
- Uvicorn
- Faker (for test users)
- pytest (for tests)

## Setup

Clone the repository:
``` bash
git clone https://github.com/<your-username>/core_ledger.git
cd core_ledger
code .
```
To checkout a specific branch:
``` bash
git checkout <branch-name>
```


Create a virtual environment:
``` bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
``` bash
pip install -r requirements.txt
```

Initialize the database:
``` bash
python3 -m tests.test_core
```

## Running Tests
python3 -m pytest -q


Tests cover:

- Core services (UserManager, QueryService)
- CLI operations
- API endpoints

## Database

- SQLAlchemy with SQLite
- Shared between CLI and web frontend
- Database files ignored in Git
- Safe session handling to prevent “database locked” errors
- Fake users can be seeded for testing

## Project Structure
```core-ledger/
├─ backend/
│  ├─ cli/                # CLI for entries
│  ├─ core/               # Database & models
│  ├─ services/           # Service layer
│  └─ __init__.py
├─ frontend/            # Web frontend
│  └─ index.html
├─ tests/              # Test scripts
├─ main.py             # FastAPI entrypoint
├─ requirements.txt
├─ README.md
├─ .gitignore
```
Author: Ayodeji Osungbohun
Project: Core Ledger
Phase 1: CLI-based system
Phase 2: CLI + Web Frontend + API integration