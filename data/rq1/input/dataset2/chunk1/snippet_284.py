#Source: https://stackoverflow.com/questions/64441507/attributeerror-callbackcontext-update-object-has-no-attribute-message
def start(bot, update):
    if update.message.from_user.username == AAA:
        bot.sendMessage(chat_id=update.message.chat_id, text="Text_one")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Text_two")
...
updater = Updater(token=bot_token)

start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)