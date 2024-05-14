#Source: https://stackoverflow.com/questions/59695431/nameerror-member-not-defined-with-discord-py
@client.command()
async def gift(ctx,*, member : discord.Member):
    with open('users.json', 'r') as f:
        users = json.load(f)

        await update_data(users, member.id)
        await add_coin(users, member.id, 1)

        with open('users.json', 'w') as f:
            users = json.dump(f)

async def update_data(users, user):
    if not member.id in users:
        users[member.id] = {}
        users[member.id]['coins'] = 0

async def add_coin(users, user, coin):
    users[member.id]['coins'] += coin
    await ctx.send(f'{member.id} has {coin} coins')