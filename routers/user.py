from uuid import UUID
import pytest
from fastapi import APIRouter, HTTPException, Response
from services.user import user_service
from schemas.user import Response, UserCreate, UserUpdate

user_router = APIRouter()

@user_router.get("")
def get_users():
    return user_service.get_all_users()

@user_router.get("/{id}")
def get_user_by_id(id: UUID):
    user = user_service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

@user_router.post("")
def add_user(user_in: UserCreate):
    user = user_service.create_user(user_in)
    return Response(message="User created successfully", data=user)

@user_router.put("/{id}")
def update_user(id: UUID, user_in: UserUpdate):
    user = user_service.update_user(id, user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return Response(message="User updated successfully", data=user)

@user_router.delete("/{id}")
def delete_user(id: UUID):
    deleted = user_service.delete_user(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found.")
    return Response(message="User deleted successfully")




# @user_router.get("/users/", tags=["users"])
# async def get_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]


# @user_router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


# @user_router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}






# @pytest.fixture
# def sample_user_data():
#     return {
#         "name": "Jane Doe",
#         "email": "jane@example.com",
#         "age": 30
#     }

# def test_add_user(sample_user_data):
#     response = client.post("/users", json=sample_user_data)
#     assert response.status_code == 200
#     json_data = response.json()
#     assert json_data["message"] == "User added successfully"
#     assert json_data["data"]["name"] == sample_user_data["name"]
#     assert "id" in json_data["data"]

# def test_get_users():
#     response = client.get("/users")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# def test_get_user_by_id(sample_user_data):
#     # Create user first
#     create_resp = client.post("/users", json=sample_user_data)
#     user_id = create_resp.json()["data"]["id"]

#     # Now get user by ID
#     get_resp = client.get(f"/users/{user_id}")
#     assert get_resp.status_code == 200
#     assert get_resp.json()["name"] == sample_user_data["name"]

# def test_update_user(sample_user_data):
#     # Create user first
#     create_resp = client.post("/users", json=sample_user_data)
#     user_id = create_resp.json()["data"]["id"]

#     # Update user
#     update_data = {
#         "name": "Jane Updated",
#         "email": "jane.updated@example.com",
#         "age": 31
#     }
#     update_resp = client.put(f"/users/{user_id}", json=update_data)
#     assert update_resp.status_code == 200
#     assert update_resp.json()["message"] == "User updated successfully"
#     assert update_resp.json()["data"]["name"] == "Jane Updated"

# def test_delete_user(sample_user_data):
#     # Create user first
#     create_resp = client.post("/users", json=sample_user_data)
#     user_id = create_resp.json()["data"]["id"]

#     # Delete user
#     delete_resp = client.delete(f"/users/{user_id}")
#     assert delete_resp.status_code == 200
#     assert delete_resp.json()["message"] == "User deleted successfully"

#     # Confirm user no longer exists
#     get_resp = client.get(f"/users/{user_id}")
#     assert get_resp.status_code == 404
