"""Query-oriented service for reading user entries.

This service exposes read and simple delete operations against the
User table. It is intentionally focused on queries so CLI and other
callers have a small API surface for read-only operations.

This is a bridge between phase 1 and all other phases as future develpment is continued.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from core.database import sessionlocal
from core.models import User


class QueryService:
    """Provides methods to retrieve User entries.

    The service attaches a session created via `sessionlocal()` and
    uses it for queries. Methods return SQLAlchemy model instances.
    """

    def __init__(self) -> None:
        self.db: Session = sessionlocal()

    def get_all_entries(self) -> List[User]:
        """Return all saved User entries as a list.
        """

        return self.db.query(User).all()

    def get_entry_by_id(self, id: int) -> Optional[User]:
        """Return a single User entry by its integer id or None if not found.
        """

        return self.db.query(User).filter(User.id == id).first()

    def delete_all(self) -> None:
        """Delete all User entry rows and commit the transaction.

        This is a destructive operation intended for tests or admin use.
        """

        self.db.query(User).delete()
        self.db.commit()
        print("All user entries have been deleted!")
        
  