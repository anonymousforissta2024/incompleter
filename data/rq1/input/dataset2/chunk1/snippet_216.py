#Source: https://stackoverflow.com/questions/64675521/endswith-method-raises-exception-attributeerror-str-object-has-no-attribu
@commands.command()
async def c(self, ctx, color: str, *, name: str):
    name_lower = name.lower()

    if name_lower.endswith("owner"):
        embed = discord.Embed(
            title=":x: Error Creating Faction",
            colour=discord.Colour.purple(),
            description="Make sure your faction name doesn't end with the word **owner**."
        )
        await ctx.send(embed=embed)
    else:
        if name_lower.endswith("faction"):
            role_name = name_lower.capitalize()
        else:
            role_name = f"{name_lower.capitalize()} Faction"

        await ctx.guild.create_role(name=role_name, color=color)
        await ctx.guild.create_role(name=f"{role_name} Owner", color=color)

        await ctx.message.add_reaction(":white_check_mark:")