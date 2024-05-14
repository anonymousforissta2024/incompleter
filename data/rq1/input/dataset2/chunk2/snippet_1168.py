#Source: https://stackoverflow.com/questions/73376735/python-telebot-issue-typeerror-telebot-send-message-missing-1-required-posit
import telebot;

bot = telebot.TeleBot('*there was my Telegram bot token*');

name = '';
surname = '';
age = 0;

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Hi! I'm another bot for practicing skill :)")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "hi":
        bot.send_message(message.from_user.id, "How can I help you?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Registration - /reg")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Nice! Lets sign you up! What is your name?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, "Sorry, I don't understand that. Write /help")
def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Okay! What is your surname?');
    bot.register_next_step_handler(message, get_surname);
def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('What is your age?');
    bot.register_next_step_handler(message, get_age);
def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Oops! I need only number.');
    bot.send_message(message.from_user.id, 'You are '+str(age)+'yo, your full name is '+name+' '+surname+'?')        

bot.delete_webhook()
bot.infinity_polling()