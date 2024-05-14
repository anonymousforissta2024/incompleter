#Source: https://stackoverflow.com/questions/68330275/fastapi-typeerror-retreive-job-got-multiple-values-for-argument-id
@router.get("/get/{id}")
def retrieve_job_by_id(id:int, id_job: job_board = Depends(get_db)):
    #print(type(session))
    job_id = job_board.retrieve_job(id_job, id=id)
    if not job_id:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    return job_id