#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from sql import crud, database, sql_models
from pydantic_models import User, Todo, UserCreation, TodoCreation


sql_models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(user=User, db: Session = Depends(get_db)):
    db_user_email = crud.get_user_by_email(db, email=user.email)
    db_user_name = crud.get_user
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD,
                            detail="Email already taken")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[User])
def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@app.post("/users/{user_id}/todo/", response_model=Todo)
def create_todo_list(user_id: int, todo: TodoCreation, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo, user_id=user_id)


@app.get("/items/", response_model=List[Todo])
def read_todo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todo(db, skip=skip, limit=limit)
    return todos