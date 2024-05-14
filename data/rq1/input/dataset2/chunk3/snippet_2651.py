#Source: https://stackoverflow.com/questions/65383456/command-raised-an-exception-nameerror-name-convert-is-not-defined
class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    def convert(time):
        pos = ["s", "m", "h", "d"]
        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}
        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    async def giveaway(self, ctx):
        await ctx.send("Answer The Following Questions For Giveaway:")

        questions = ["Channel For Giveaway?",
                     "Duration Of Giveaway? (s , m , h , d)",
                     "Prize Of Giveaway?"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(i)

            try:
                msg = await self.client.wait_for('message', timeout=20.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send('You Did Not Answer In Time!')
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f'Mention Channel Properly! Example: {ctx.channel.mention}')
            return

        channel = self.client.get_channel(c_id)

        time = convert(answers[1])
        if time == -1:
            await ctx.send(f'Answer Time With A Proper Unit (s, m, h, d)')
            return
        elif time == -2:
            await ctx.send(f'Time Must Be A Integer!')
            return

        prize = answers[2]

        await ctx.send(f'Giveaway Will Be In Channel {channel.mention} And Will Last {time}.')

        embed = discord.Embed(title="🎉Giveaway🎉", description=f"{prize}", color=ctx.author.color)
        embed.add_field(name="Hosted by:", value= ctx.author.mention)
        embed.set_footer(text=f"Ends after {answers[1]} from now. ")

        g_msg = await channel.send(embed=embed)

        await g_msg.add_reaction("🎉")

        await asyncio.sleep(time)

        new_msg = await channel.fetch_message(g_msg.id)

        users = await g_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        await channel.send(f'Congrats! {winner.mention} won {prize}!')