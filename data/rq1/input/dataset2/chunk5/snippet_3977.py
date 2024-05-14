#Source: https://stackoverflow.com/questions/51348243/python-async-redis-gives-error-attributeerror-aexit
from sanic import Sanic
from sanic.response import json
import redis

app = Sanic()

# request.args['token']

@app.route('/<id>')
async def test(request, id):
    async with redis.StrictRedis(host='0.0.0.0', port=6379, db=0) as r:
        data = await r.get("test")
        # print(data)

    return json({
        'data': data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988)