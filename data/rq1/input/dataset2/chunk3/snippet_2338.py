#Source: https://stackoverflow.com/questions/68330275/fastapi-typeerror-retreive-job-got-multiple-values-for-argument-id
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends

from db.repository.job_board_dal import job_board
from schemas.jobs import JobCreate, ShowJob
from db.repository.job_board_dal import Job
from depends import get_db

router = APIRouter()

@router.post("/create-job",response_model=ShowJob)
async def create_user(Job: JobCreate, jobs: Job = Depends(get_db)):
    owner_id = 1
    return await jobs.create_new_job(Job, owner_id)

@router.get("/get/{id}")
def retrieve_job_by_id(id:int, job_board = Depends(get_db)):
    #print(type(session))
    job_id = job_board.retrieve_job(job_board, id=id)
    if not job_id:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    return job_id