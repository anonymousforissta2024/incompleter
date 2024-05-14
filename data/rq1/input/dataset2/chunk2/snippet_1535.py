#Source: https://stackoverflow.com/questions/76454850/attributeerror-property-object-has-no-attribute-get-when-using-depends-in
@app.get("/")
async def home(user: Annotated[User, Depends(authenticate_request(Request))]):
    """
    status _summary_
    Returns status message if service is running
    """
    if isinstance(user, User):
        return {"Welcome, service is running ok!"}
    raise HTTPException(
        status_code=401,
        detail="User not authorized!",
    )