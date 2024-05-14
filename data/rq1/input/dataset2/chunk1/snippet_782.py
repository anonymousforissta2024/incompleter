#Source: https://stackoverflow.com/questions/33473140/attributeerror-module-object-has-no-attribute-ensure-future
import asyncio
import aiohttp
import json
import logging

# async def fetch_content(url, symbols):
# yield from  aiohttp.post(url, symbols=symbols)

@asyncio.coroutine
def fetch_page(writer, url, data):
   response = yield from aiohttp.post(url, data=data)
   resp = yield from response.read_and_close()
   print(resp)
   writer.write(resp) 
   return           


@asyncio.coroutine
def process_payload(writer, data, scale):
   tasks = []
   data = data.split('\r\n\r\n')[1]
   data = data.split('\n')
   data = [x.split(':') for x in data]
   print(data)
   data = {x[0]: x[1] for x in data}
   print(data)                 
   # data = data[0].split(':')[1]
   data = data['symbols']
   print(data)
   data = data.split(',')
   data_len = len(data)
   data_first = 0
   data_last = scale
   url = 'http://xxxxxx.xxxxxx.xxx/xxxx/xxxx'
   while data_last < data_len:
       tasks.append(asyncio.ensure_future(fetch_page(writer, url,{'symbols': ",".join(data[data_first:data_last])})))
       data_first += scale
       data_last += scale 

   tasks.append(asyncio.ensure_future(fetch_page(writer, url,{'symbols': ",".join(data[data_first:data_last])})))
   loop.run_until_complete(tasks)    
   return 

@asyncio.coroutine
def process_url(url):
    pass

@asyncio.coroutine
def echo_server():
  yield from asyncio.start_server(handle_connection, 'xxxxxx.xxxx.xxx', 3000)

@asyncio.coroutine
def handle_connection(reader, writer):
   data = yield from reader.read(8192)

   if data:
        message =  data.decode('utf-8')
        print(message)
        yield from process_payload(writer, message, 400)

   writer.write_eof()   
   writer.close()


#url = 'http://XXXXXXX.xxxxx.xxx/xxxx/xxxxxx/xxx'
data = {'symbols': 'GD-US,14174T10,04523Y10,88739910,03209R10,46071F10,77543110,92847N10'}

loop = asyncio.get_event_loop()
loop.run_until_complete(echo_server())
try:
    loop.run_forever()
finally:
    loop.close()