#Source: https://stackoverflow.com/questions/73524142/typeerror-an-integer-is-required-got-type-str-in-discord-py
@client.command(aliases=['bal'])
async def balance(ctx):

  with open("balance.json", "r") as bal:
    
    user = ctx.author
    users = await get_balance_data()#line-45
    balance = users[str(user.id)]["balance"] = 0
    
    embedbalance = discord.Embed(titles=f"{ctx.author.name}'s balance", color=discord.Color.blue())
    embedbalance.add_field(name="balance", value=balance)
    await ctx.send(embed=embedbalance)
  
  
async def get_balance_data():
  with open("balance.json", "w") as balance: #line-54
    users = json.loads(balance.read())
    json.dump(users, balance)

  return users

client.run(token)