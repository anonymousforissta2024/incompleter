#Source: https://stackoverflow.com/questions/67511899/attributeerror-nonetype-object-has-no-attribute-send-when-i-try-to-send-a
import time, random, discord
from datetime import datetime
from discord.ext import commands


async def time_messege(args):
    bot = commands.Bot(command_prefix='.')
    alarmtime = "19:36"
    
    greeting_channel = bot.get_channel("814238156396298310")
    #channel = bot.get_channel = xxx

    #client = discord.Client()


    while True:
      
        lcltime = datetime.now().strftime('%H:%M')

        if lcltime == alarmtime:

            #aca pondria el code de detectar canal y enviar
            print("is time!")

            random_num = random.randint(1, 4)

            if random_num == 1:
                await greeting_channel.send("Holi!, como estan chic@s?")
                #await client.send_message(discord.Object(id='814238156396298310'), "Holi!, como estan chic@s?")
            elif random_num == 2:
                await greeting_channel.send("Holi!, oCmo va su dia? que me cuentan?")
                #await client.send_message(discord.Object(id='814238156396298310'), "Holi!, oCmo va su dia? que me cuentan?")
            elif random_num == 3:
                await greeting_channel.send("Holi!, Como va su dia? que andan haciendo?")
                #await client.send_message(discord.Object(id='814238156396298310'), "Holi!, Como va su dia? que andan haciendo?")
            elif random_num == 4:
                await greeting_channel.send("Holi!, como se encuentran?")
                #await client.send_message(discord.Object(id='814238156396298310'), "Holi!, como se encuentran?")

            time.sleep(90)

        else:
            print("not yet")
            time.sleep(10)