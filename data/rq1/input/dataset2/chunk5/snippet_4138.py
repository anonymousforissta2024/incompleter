#Source: https://stackoverflow.com/questions/39553483/attributeerror-module-discordoragisearch-has-no-attribute-isvalidmessage
import DiscordoragiSearch

...

@Discord.client.event
async def on_message(message):
    print('Message recieved')
    #Is the message valid (i.e. it's not made by Discordoragi and I haven't seen it already). If no, try to add it to the "already seen pile" and skip to the next message. If yes, keep going.
    if not (DiscordoragiSearch.isValidMessage(message)):
        try:
            if not (DatabaseHandler.messageExists(message.id)):
                DatabaseHandler.addMessage(message.id, message.author.id, message.server.id, False)
        except Exception:
            traceback.print_exc()
            pass
    else:
        await process_message(message)