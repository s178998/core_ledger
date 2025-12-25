from typing import Callable, Dict, Optional
from sqlalchemy.orm import Session
from backend.core.database import Base, sessionlocal, engine
from backend.core.models import User

# Ensure tables exist
Base.metadata.create_all(bind=engine)

class UserManager:
    def __init__(self) -> None:
        self.db: Session = sessionlocal()

    def create_user_with_confirmation(
        self, user_data: Dict[str, str], confirm_callback: Callable[[User], bool]
    ) -> Optional[int]:
        user = User(**user_data)
        if not confirm_callback(user):
            return None
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user.id
        except Exception:
            self.db.rollback()
            raise

    def delete_all_entries(self) -> None:
        self.db.query(User).delete()
        self.db.commit()
        print("All entries deleted!")
