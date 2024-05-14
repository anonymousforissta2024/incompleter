#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from sqlalchemy.orm import Session

from . import sql_models
import pydantic_models

# Get single user
def get_user(db: Session, user_id: int):
    return db.query(sql_models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, username: str):
    return db.query(sql_models.User).filter(models.User.username == username).first()

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(sql_models.User).filter(models.User.email == email).first()

# Get all users
def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.User).offset(skip).limit(limit).all()

# Create a user
def create_user(db: Session, user: pydantic_models.UserCreation):
    fake_hashed_password = user.password + "fakehash" # Hashed user's password
    db_user = sql_models.User(username=user.username, email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_todo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: pydantic_models.TodoCreation, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item