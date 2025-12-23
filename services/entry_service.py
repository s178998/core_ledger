"""Service for creating and managing user entries.

This module contains a lightweight manager used by the CLI to create
and manipulate User objects persisted via SQLAlchemy.
"""

from typing import Callable, Dict, Optional

from sqlalchemy.orm import Session

from core.database import Base, sessionlocal, engine
from core.models import User

# Ensure tables are created when service module is imported
Base.metadata.create_all(bind=engine)


class UserManager:
    """Manage user creation and deletion.

    The implementation uses a session created from `sessionlocal()` and
    performs simple commit/refresh operations. It intentionally keeps
    responsibilities small so the logic remains easy to test.
    """

    def __init__(self) -> None:
        self.db: Session = sessionlocal()

    def create_user_with_confirmation(
        self, user_data: Dict[str, str], confirm_callback: Callable[["User"], bool]
    ) -> Optional[int]:
        """Create an entry after asking the caller to confirm the populated object.

        Args:
            entry_data: Mapping of user field names to values.
            confirm_callback: Callable that receives the created User instance
                and returns True to persist or False to cancel.

        Returns:
            The created user's entry integer id on success, or None when the
            confirmation callback declines to persist.
        """

        user = User(**user_data)

        if not confirm_callback(user):
            return None
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user.id
        except Exception:
            raise

    def delete_all_entries(self) -> None:
        """Remove all entries from the database (destructive).

        Intended for administrative or test cleanup use.
        """

        self.db.query(User).delete()
        self.db.commit()
        print("All entries have been deleted!")



