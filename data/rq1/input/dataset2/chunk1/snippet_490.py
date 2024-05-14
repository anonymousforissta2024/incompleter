#Source: https://stackoverflow.com/questions/68053973/typeerror-cannot-pickle-module-object-in-fastapi
from fastapi import APIRouter, HTTPException, status, Depends

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ..modules import oauth_module
from ..models.user_model import User
from ..schemas import token_schema

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

...

@router.get("/my_info")
async def read_user_info(current_user: User = Depends(oauth_module.get_current_active_user)):
    return current_user