#Source: https://stackoverflow.com/questions/64441507/attributeerror-callbackcontext-update-object-has-no-attribute-message
def rating(bot, update):
    bot.send_sticker(chat_id,'some_sticker_id')
...
rating_handler = CommandHandler('rating', rating)
updater.dispatcher.add_handler(rating_handler)