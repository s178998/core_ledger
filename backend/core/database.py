"""Database configuration and SQLAlchemy helpers.

This module defines the database URL, the SQLAlchemy engine, a
session factory and the declarative base used by ORM models.
"""

from typing import Callable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import Engine

DATABASE_URL: str = "sqlite:///./core_ledger.db"

engine: Engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
sessionlocal: Callable = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
