import uuid
import pytest
from schemas.user import UserUpdate, UserCreate, User
from database import user
from services.user import user_service, users


@pytest.fixture(autouse=True)
def clear_users():
    """Reset users list before each test"""
    users.clear()


@pytest.fixture
def sample_user_create():
    return UserCreate(
        name="Alice",
        email="alice@example.com",
        age=28
    )


def test_create_user(sample_user_create):
    user = user_service.create_user(sample_user_create)

    assert user.name == sample_user_create.name
    assert user.email == sample_user_create.email
    assert user.age == sample_user_create.age
    assert isinstance(user.id, uuid.UUID)



def test_get_user_by_id(sample_user_create):
    user = user_service.create_user(sample_user_create)
    fetched = user_service.get_user_by_id(user.id)

    assert fetched is not None
    assert fetched.id == user.id


def test_get_user_by_id_not_found():
    fake_id = uuid.uuid4()
    user = user_service.get_user_by_id(fake_id)
    assert user is None


def test_update_user(sample_user_create):
    user = user_service.create_user(sample_user_create)

    update_data = UserUpdate(name="Alice Updated", age=30)
    updated_user = user_service.update_user(user.id, update_data)

    assert updated_user.name == "Alice Updated"
    assert updated_user.age == 30
    assert updated_user.email == sample_user_create.email  # unchanged


def test_update_user_not_found():
    fake_id = uuid.uuid4()
    update_data = UserUpdate(name="Ghost")
    updated = user_service.update_user(fake_id, update_data)

    assert updated is None


def test_delete_user(sample_user_create):
    user = user_service.create_user(sample_user_create)
    result = user_service.delete_user(user.id)

    assert result is True
    # assert len(user) == 0


def test_delete_user_not_found():
    fake_id = uuid.uuid4()
    result = user_service.delete_user(fake_id)

    assert result is False
