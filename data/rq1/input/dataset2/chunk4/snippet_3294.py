#Source: https://stackoverflow.com/questions/77129857/typeerror-when-initializing-updater-in-python-telegram-bot
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import telegram.ext.filters as filters
from pytube import YouTube

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a YouTube link with /download to get the video.')

def download_video(update: Update, context: CallbackContext) -> None:
    url = context.args[0]
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    filename = f"{yt.title}.mp4"
    os.rename(video.default_filename, filename)
    update.message.reply_document(document=open(filename, 'rb'))
    os.remove(filename)

def main() -> None:
    updater = Updater(token='646XXXXXXXXXXXXXXXXXXXXXXXXXmQM', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('download', download_video, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()