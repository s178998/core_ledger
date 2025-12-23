"""Database configuration and SQLAlchemy helpers.

This module defines the database URL, the SQLAlchemy engine, a
session factory and the declarative base used by ORM models.
"""

from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL: str = "sqlite:///./core_ledger.db"

# SQLAlchemy engine for the application
engine: Engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory — call to create a new Session instance
sessionlocal: Callable = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Declarative base for ORM models
Base = declarative_base()