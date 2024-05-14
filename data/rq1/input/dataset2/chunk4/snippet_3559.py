#Source: https://stackoverflow.com/questions/72251386/typeerror-object-of-type-coroutine-is-not-json-serializable
import configparser
import json
import datetime

from telethon.sync import TelegramClient , events
from telethon import connection


from datetime import date, datetime


from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


from telethon.tl.functions.messages import GetHistoryRequest


config = configparser.ConfigParser()
config.read("config.ini")


api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
bot__token = config['Telegram']['bot_token']

client = TelegramClient( username, api_id, api_hash )
bot = TelegramClient( 'bot' , api_id , api_hash ).start( bot_token = bot__token )


current_action = ''

async def dump_all_messages(channel):
    offset_msg = 0 
    limit_msg = 100
    
    all_messages = []
    total_messages = 0
    total_count_limit = 2
    
    class DateTimeEncoder(json.JSONEncoder):
        
        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, bytes):
                return list(o)
            return json.JSONEncoder.default(self, o)
                
    while True:
        history = await client( GetHistoryRequest (
                peer=channel,
                offset_id=offset_msg,
                offset_date=None,
                add_offset=0,
                limit=limit_msg, 
                max_id=0, 
                min_id=0,
                hash=0
            )
        )
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
        
    with open('channel_messages.json', 'w', encoding='utf8') as outfile:
        json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)



@bot.on( events.NewMessage )
async def list( event ):
    match current_action:
        case '/tracking':
            channel = await client.get_entity( event.message.message )
            await dump_all_messages( channel )
            raise events.StopPropagation


@bot.on( events.NewMessage( pattern = '/tracking' ) )
async def link(event):
    global current_action
    current_action = '/tracking'
    await event.respond('I\'m expecting a link')
    raise events.StopPropagation

client.start()
bot.run_until_disconnected( )