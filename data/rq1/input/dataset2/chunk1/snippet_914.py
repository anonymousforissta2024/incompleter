#Source: https://stackoverflow.com/questions/75825362/attributeerror-encode-when-returning-streamingresponse-in-fastapi
from fastapi import APIRouter, FastAPI, Header

from src.chat.completions import chat_stream
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get("/v1/completions",response_class=StreamingResponse)
def stream_chat(q: str, authorization: str = Header(None)):
    auth_mode, auth_token = authorization.split(' ')
    if auth_token is None:
        return "Authorization token is missing"
    answer = chat_stream(q, auth_token)
    return StreamingResponse(answer, media_type="text/event-stream")