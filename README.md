# Core Ledger (Phase 1)

**Core Ledger** is a lightweight Python-based ledger and user entry system. This repository contains the core logic, services, and CLI to create, query, and manage user entries.  

## Disclaimer
Some features are commented out due to this being only phase one.
For future development, features will be uncommented for the implementation of other phases.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Database](#database)
- [Project Structure](#project-structure)

---

## Features

- CLI for creating and querying user entries
- Modular service architecture (`core`, `services`, `cli`)
- Database management using SQLAlchemy
- Automated testing for core functionality
- Utility scripts for generating and deleting test data

---

## Requirements

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)
- SQLAlchemy
- Faker (for generating test users)
- pytest (for testing)

---

## Setup

1. **Clone the repository**:

```bash
git clone https://github.com/<your-username>/core_ledger.git
cd core_ledger
```

## Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
## Install dependencies:
```bash
pip install -r requirements.txt
python3 -m tests.test_core
```

Initialize the database (SQLite):
```bash
python3 -m tests.test_core

```
## Usage

Run the CLI:

```bash
python3 -m cli.main
```

Available actions via CLI:
- Add a new user entry
- Query users
- Delete entries (for testing purposes)

## Running Tests
```bash
python3 -m pytest -q
```
Ensures the core functions and services behave correctly.
Includes tests for database queries, services, and CLI functionality.

## Database
- Uses SQLAlchemy with SQLite.
- Database files (*.db) are ignored in Git (.gitignore) to avoid large commits.
- For testing or research purposes, fake users can be seeded via tests/test_entry_services.py.

## Project Structure
```core-ledger/
│
├─ cli/                # Command-line interface
├─ core/               # Core database and models
├─ services/           # Service layer for entries
├─ tests/              # Test scripts
├─ .gitignore
├─ README.md
├─ requirements.txt
```
Author: Ayodeji Osungbohun
Phase: 1 (Core Ledger)
