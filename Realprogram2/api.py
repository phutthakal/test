from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, BackgroundTasks
from models import User, UserUpdateRequest
import time

app = FastAPI()

db: List[User] = [
    User(
        id=UUID('ecc530d9-185b-4836-9cb0-76e69d3ded7b'), 
        license_plate="กก2893", 
        height=199)
]

@app.get("/api/test/users")
async def fetch_users():
    return db

@app.post("/api/test/users")
async def lastest_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.put("/api/test/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.license_plate is not None:
                user.license_plate = user_update.license_plate
            if user_update.height is not None:
                user.height = user_update.height
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does exit"
    )

@app.delete("/api/test/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does exit"
    )