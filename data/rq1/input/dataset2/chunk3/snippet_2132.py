#Source: https://stackoverflow.com/questions/71012290/switching-to-routers-in-fastapi-did-not-go-well-response-model-list-pydantic
import models
from database import get_db

router: APIRouter = APIRouter()


@router.get("/postss", response_model=List[models.Post])
def get_post(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)

    try:
        posts = db.query(models.Post).all()
    except Exception as ex:
        msg = f"Unexpected {ex=}, {type(ex)=}"
        raise HTTPException(status_code=500, detail=msg)
    return posts