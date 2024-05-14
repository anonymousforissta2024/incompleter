#Source: https://stackoverflow.com/questions/77414673/how-do-i-fix-a-type-error-missing-annotation-for-my-discord-bot-python-3
@app_commands.command(name='kick', description='Kicks the member of your choice if you have kick permissions.')
@has_permissions(kick_members=True)
async def kick(s, interaction:discord.Interaction, member:discord.Member, *, reason='None'):
    await interaction.response.send_message(f'User {member} has been kicked.')
    await member.kick(reason=reason)
@kick.error
async def kick_error(s, interaction:discord.Interaction, error):
    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message('You don\'t have permission to kick people!')