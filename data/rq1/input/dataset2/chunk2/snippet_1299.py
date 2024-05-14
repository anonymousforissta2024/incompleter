#Source: https://stackoverflow.com/questions/44007989/attributeerror-generator-object-has-no-attribute-connect-pydle-asyncio
@asyncio.coroutine
class MyOwnBot(pydle.Client):
     async def on_connect(self):
        await self.join('#new')

iclient = MyOwnBot('testeee', realname='tester')
loop = asyncio.get_event_loop()
asyncio.ensure_future(iclient.connect('irc.test.net', 6697, tls=True,tls_verify=False), loop=loop)