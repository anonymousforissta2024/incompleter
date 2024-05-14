#Source: https://stackoverflow.com/questions/71012290/switching-to-routers-in-fastapi-did-not-go-well-response-model-list-pydantic
import models
import schemas
from database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


@app.get("/")
async def root():
    return {"message": "Welcome To My Api!"}


@app.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)

    try:
        posts = db.query(models.Post).all()
    except Exception as ex:
        msg = f"Unexpected {ex=}, {type(ex)=}"
        raise HTTPException(status_code=500, detail=msg)
    return posts