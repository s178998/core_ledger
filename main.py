from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.services.entry_service import UserManager
from backend.services.query_service import QueryService
from backend.core.models import User
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Core Ledger API")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
um = UserManager()
qs = QueryService()

# Pydantic schema for API
class UserSchema(BaseModel):
    first_name: str
    last_name: str
    phone: str
    sex: str
    tshirt_size: str
    
@app.get("/")
def root():
    return {"message": "Server is running"}

@app.post("/users/")
def create_user(user: UserSchema):
    def confirm(u: User):
        return True  # API auto-confirms

    user_id = um.create_user_with_confirmation(user.model_dump(), confirm)
    if user_id:
        return {"status": "success", "user_id": user_id}
    raise HTTPException(status_code=400, detail="Failed to create user")

@app.get("/users/")
def get_all_users():
    users = qs.get_all_entries()
    return [
        {
            "id": u.id,
            "first_name": u.first_name,
            "last_name": u.last_name,
            "phone": u.phone,
            "sex": u.sex,
            "tshirt_size": u.tshirt_size,
        }
        for u in users
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = qs.get_entry_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "sex": user.sex,
        "tshirt_size": user.tshirt_size,
    }


if __name__ == "__main__":
    uvicorn.run(app)