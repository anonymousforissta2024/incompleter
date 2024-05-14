#Source: https://stackoverflow.com/questions/68656152/command-raised-an-exception-attributeerror-nonetype-object-has-no-attribute
@client.command(aliases=["lb"])
async def leaderboardie(ctx, x=1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(title=f"Top {x} Richest People",
                       description="This is decided on the basis of raw money in the bank and wallet", color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}",  inline=False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed=em)