#Source: https://stackoverflow.com/questions/71104277/discord-py-typeerror-command-name-error-missing-1-required-positional-argumen
# COG CLASS
class Entries(commands.Cog):

    def __init__(self, client):
        self.client = client

# START UP
    @commands.Cog.listener()
    async def on_ready(self):
        print('Entry.py is connected.')

# ENTER COMMAND
    @commands.command(name="entry", aliases=["enter","Enter","ENTER"])
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def entry(self, ctx):
        filename = "entries.txt"
        with open(filename, "a") as file: 
            file.write(f"{ctx.author.name}\n")
            await ctx.send(f"**@{ctx.author.name} Your entry has been recorded. :white_check_mark:**")

    @entry.error
    async def command_name_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"**@{ctx.author.name} You have already entered! :warning:**")

# STOP COMMAND
    @commands.command()
    async def stop(self, ctx, *, command):
        command = self.client.get_command(command)
        command.update(enabled=False)
        await ctx.author.send(f" The command **!enter** has been **disabled**.")
        await ctx.channel.purge(limit=1)

# START COMMAND
    @commands.command()
    async def start(self, ctx, *, command):
        command = self.client.get_command(command)
        command.update(enabled=True)
        await ctx.author.send(f" The command **!enter** has been **enabled**.")
        await ctx.channel.purge(limit=1)

def setup(client):
    client.add_cog(Entries(client))