#Source: https://stackoverflow.com/questions/70147604/discord-ext-commands-errors-commandinvokeerror-command-raised-an-exception-att
@client.event
async def on_ready():
    changeStatus.start()
    kvuqqs = client.get_channel(906998823187017728)
    librar = client.get_channel(906168716197232660)

    await kvuqqs.send('Айоу! Бот был включен. \nК сожалению, на данный момент обновлений нет. \n`l.хелп`')
    await librar.send(embed=discord.Embed(title='Бот был включен!', description='Версия бота на данный момент: 2.0.1.', color=random.choice(colors)))