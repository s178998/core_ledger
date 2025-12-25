from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.models import Base
from backend.services.entry_service import UserManager
from backend.services.query_service import QueryService

def make_test_session():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    return Session()

def test_query_service_empty():
    session = make_test_session()
    qs = QueryService()
    qs.db = session
    assert qs.get_all_entries() == []

def test_user_manager_create_and_query():
    session = make_test_session()
    um = UserManager()
    um.db = session
    qs = QueryService()
    qs.db = session

    def confirm(u): return True

    user_data = {
        "first_name": "Alice",
        "last_name": "Smith",
        "phone": "1234567890",
        "sex": "F",
        "tshirt_size": "M"
    }

    user_id = um.create_user_with_confirmation(user_data, confirm)
    entry = qs.get_entry_by_id(user_id)
    assert entry.first_name == "Alice"
