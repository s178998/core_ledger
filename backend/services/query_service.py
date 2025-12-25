from typing import List, Optional
from sqlalchemy.orm import Session
from backend.core.database import sessionlocal
from backend.core.models import User

class QueryService:
    def __init__(self) -> None:
        self.db: Session = sessionlocal()

    def get_all_entries(self) -> List[User]:
        return self.db.query(User).all()

    def get_entry_by_id(self, id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == id).first()

    def delete_all(self) -> None:
        self.db.query(User).delete()
        self.db.commit()
        print("All user entries deleted!")
