#Source: https://stackoverflow.com/questions/66682539/economy-bot-discord-py-rewrite-leaderboard-error-attributeerror-nonetype
@client.command(aliases = ["lb"])
async def leaderboard(ctx,x: int = 10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(title=f"Top {x} Richest People", color=random.randint(0, 0xffffff))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = ctx.guild.get_member(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index += 1
    await ctx.send(embed=em)