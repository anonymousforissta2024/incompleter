#Source: https://stackoverflow.com/questions/76367183/command-reload-raised-an-exception-typeerror-botbase-reload-extension-miss
@bot.event
async def on_ready():
        print(f'Logged in as {bot.user.name}')
        for guild in bot.guilds:
            print(f"Bot is in {guild.name} with {guild.member_count} members")
        bot.remove_command('help')
        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                extensions = f"extension.{cmd_file.name[:-3]}"
                await bot.load_extension(extensions)
                print(f"Loaded extension: {extensions}")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} slash commands\n")
        except Exception as e:
            print(f"Failed to sync slash commands: {e}")