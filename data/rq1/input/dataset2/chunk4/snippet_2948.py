#Source: https://stackoverflow.com/questions/65083342/error-handler-raising-an-exception-type-error-on-discord-py
@commands.command(name='clear', aliases=['clean', 'cleanup'])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def clear(self, ctx, message, limit: int = 10) -> None:
        await ctx.message.add_reaction("<:tars_certo:783051315764133910>")
        time.sleep(2)
        messages = await ctx.channel.purge(bulk=True, limit=limit)
        embed=discord.Embed(title=f"`{len(messages)}` mensagens deletadas com sucesso", color=COR_PRINCIPAL)
        embed.set_author(name="Plugin de comandos do TARS",icon_url=ICONE)
        await ctx.send(embed=embed, delete_after=5)

@clear.error
async def clear_error(ctx, error):
  if isinstance(error, MissingPermissions):
        embed=discord.Embed(title="<:tars_x:783051246776877057> Erro: Você não tem permissão para usar este comando", color=COR_PRINCIPAL)
        embed.set_author(name="TARS help",icon_url=ICONE)
        await ctx.send(embed=embed)