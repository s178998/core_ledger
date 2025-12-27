""" This is just a research/database testing file has nothing to do with the project."""

from faker import Faker
import uuid
from backend.tests.test_core import User, sessionlocal, engine

class UserManager:
    def __init__(self):
        self.db = sessionlocal()
        self.faker = Faker()


    def create_fake_users(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        phone = self.faker.msisdn()[0:12]
        sex = self.faker.random_element(["M", "F"])
        tshirt_size = self.faker.random_element(["S", "M", "L", "XL", "XXL"])
        
        
        user = User(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            sex=sex,
            tshirt_size=tshirt_size
        )
        
        self.db.add(user)
        return user

    def seed_users(self, n=100):
        for i in range(n):
            reg = self.create_fake_users()
            print(f"Entry {i + 1} added: {reg.first_name} {reg.last_name}")
        self.db.commit()
        print(f"{n} random users added successfully.")
        return n
        
    def get_entry(self, id):
        entry = self.db.query(User).filter(User.id == id).first()
        print(f"\nFirst name: {entry.first_name}")
        print(f"Last name: {entry.last_name}")
        print(f"Phone: {entry.phone}")
        print(f"sex: {entry.sex}")
        print(f"Tshirt size: {entry.tshirt_size}", end="\n\n")
            
    def delete_all(self):
        query = self.db.query(User).delete()
        commit = self.db.commit()
        print("all entries deleted.")
        return query, commit
    
    def delete_range_after_million(self):
        subq = {
            self.db.query(User.id).filter(User.id > 1000000).order_by(User.id).limit(100000).subquery()
        }
       
        query = self.db.query(User).filter(User.id.in_(subq)).delete(synchronize_session=False)
        if query:
           print("Storage full. 100,000 rows deleted")
        commit = self.db.commit()
        return query, commit
    
    def get_db_count(self):
       return self.db.query(User).count()
    
if __name__ == "__main__":
    from backend.tests.test_core import Base
    Base.metadata.create_all(bind=engine)
    um = UserManager()
    
    # Test for limited storage and deletion upon no more storage.
    # So if this were to become a user led system,
    # storage limits may apply for business logic.

    # Optional: clear the DB before testing
    deleted = um.delete_all()
    print(f"All entries deleted. Total deleted: {deleted[0]}")

    # Seed initial users
    initial_seed = 100
    print(f"\nSeeding {initial_seed} users...")
    um.seed_users(n=initial_seed)

    # Get current user count
    count = um.get_db_count()
    print(f"Total users in DB after initial seed: {count}")

    # If user count exceeds 1,000,000, delete a range
    if count > 1000000:
        print("Database exceeded 1,000,000 users. Deleting 100,000 entries...")
        um.delete_range_after_million()
    else:
        # Seed more users in safe batches
        additional_seed = 5000
        print(f"Seeding additional {additional_seed} users...")
        um.seed_users(n=additional_seed)

    # Safely retrieve and print some sample entries
    sample_ids = [1000, 2000, 3000, 4000, 5000]
    print("\nFetching sample entries:")
    for uid in sample_ids:
        um.get_entry(id=uid)

    
    