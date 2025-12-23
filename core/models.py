"""ORM models for the Core Ledger application.

This module contains SQLAlchemy declarative models used by the
service and CLI layers.
"""

from sqlalchemy import Column, Integer, String, DateTime
from core.database import Base
import datetime


class User(Base):
    """Represents a persisted user entry.

    Attributes correspond to database columns and are defined with
    SQLAlchemy Column objects so they are available on instances.
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(12), nullable=False)
    sex = Column(String(4), nullable=False, default="M")
    tshirt_size = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
