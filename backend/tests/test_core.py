from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./core_test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


from sqlalchemy import Column, Integer, String, DateTime
import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(12), nullable=False)
    sex = Column(String(4), nullable=False, default="M")
    tshirt_size = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    