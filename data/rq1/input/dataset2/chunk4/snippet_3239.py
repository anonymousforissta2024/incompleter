#Source: https://stackoverflow.com/questions/74661159/building-tg-bot-with-python-giving-me-typeerror-module-object-is-not-callabl
import telegram.ext

Token = "API_KEY"

updater = telegram.ext.updater("API_KEY", use_context = True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Thanks for messaging me!")

def help(update, context):
    update.message.reply_text(
        """
        /aboutme -> More info about me.
        /jobs -> See all my open jobs!
        /myinfo -> My email information.
        /latamsalaries -> Current LATAM salaries for devs.
        """
    )

def aboutme(update, context):
    update.message.reply_text("My name is Robert Grootjen, and I'm a technical headhunter! My mission is to connect the best talent in Latin America with topnotch companies in the United States and Canada.")

def jobs(update, context):
    update.message.reply_text("")

def myinfo(update, context):
    update.message.reply_text("Linkedin: https://www.linkedin.com/in/robert-grootjen-08a10b15a/")

def latamsalaries(update, context):
    update.message.reply_text("Jr - $1500 - $3000 USD")


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('aboutme', aboutme))
dispatcher.add_handler(telegram.ext.CommandHandler('jobs', jobs))
dispatcher.add_handler(telegram.ext.CommandHandler('myinfo', myinfo))
dispatcher.add_handler(telegram.ext.CommandHandler('latamsalaries', latamsalaries))

updater.start_polling()
updater.idle()