#Source: https://stackoverflow.com/questions/64754301/uncaught-typeerror-cannot-read-property-sid-of-undefined
import asyncio
from aiohttp import web
import socketio
from aiohttp_middlewares import cors_middleware
from aiohttp_middlewares.cors import DEFAULT_ALLOW_HEADERS
sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app=web.Application()
sio.attach(app)

async def index(request):
    return web.Response(text="hello", content_type='text/html')

@sio.event
async def connect(sid, environ):
    print('Client connected',sid)
    await sio.emit('message', "good")

@sio.event
def disconnect(sid):
    print('Client disconnected',sid)

@sio.on('message')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    print(message)

app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)