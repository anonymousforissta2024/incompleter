#Source: https://stackoverflow.com/questions/54204828/function-say-throws-up-an-attributeerror-str-object-has-no-attribute-chann
@bot.command()
async def say(message):
  #await bot.delete_message(message)
  await bot.send_message(message.channel, message)