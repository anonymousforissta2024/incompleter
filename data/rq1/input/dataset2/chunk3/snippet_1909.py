#Source: https://stackoverflow.com/questions/63019333/getting-nameerror-while-importing-a-module
from bot import T_bot

update_id= None

def make_reply(msg):
    reply= 'okay'
    return reply

update_id= None

while True:
    
    updates= T_bot.gett(self, offset= update_id)
    updates= updates["result"]
    if updates:
        for item in updates:
            update_id= item['update_id']
            try:
                message= item['message']['text']
            except:
                message= None
                fromm= item['message']['from']['id']
                reply= make_reply(message)
                T_bot.send(reply, fromm)