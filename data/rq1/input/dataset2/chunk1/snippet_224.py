#Source: https://stackoverflow.com/questions/62862039/typeerror-descriptor-strftime-for-datetime-date-objects-doesnt-apply-to-a
@client.command()
async def nitrosince(ctx, member: discord.Member, guild: discord.Guild = None):
  member = ctx.member if not member  else member
  guild = ctx.guild if not guild else guild

  embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="NitroSince Command",
        
    )

  embed.add_field(name=f"{member} Has had Nitro Since:", value = datetime.date.strftime(member.premium_since, '%a, %b %d %Y')

)
  embed.set_footer(text="I was made by Grenade Visuals#0001", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)