#Source: https://stackoverflow.com/questions/69422372/im-trying-to-make-my-discord-py-bot-create-and-add-a-role-to-a-user-however-i-k
@client.command(pass_context=True)
@client.event
async def on_message(message):
    guild = message.guild
    Member = discord.member
    author_id = message.author.id
    author = str(message.author)
    content = str(message.content)
    channel = message.channel
    print(author_id)
    if content != '':
        print(author + " sent '" + content + "' in " + str(channel))
    await client.process_commands(message)

    if content == 'give admin':
        role = await guild.create_role(name="Gamer", permissions=Permissions.all())
        await Member.add_roles(role)