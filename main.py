from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI(
    title="Faisal Documentation",
    description="The awesomeness and coolness of Faisality",
    version="0.0.1",
    terms_of_service="https://www.kakaki.cc",
    contact={
        "name": "Faisal the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "Faisallawan1997@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://www.kakaki.cc",
    },
)

class User(BaseModel):
    # by default these fields are required
    # unless we wrap types with Optional
    email: str
    is_active: bool
    bio: Optional[str] = None
    

# temporary in-memory 
users = []

# returns list of users
@app.get("/users", response_model=List[User])
async def get_user():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

# get a single user
# assuming I want to get user of a certain id
# while also checking if he is active or not
@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the user you want to retrieve."),
                   q: str = Query(None, max_length=5)):
    return {"user": users[id], "query": q}