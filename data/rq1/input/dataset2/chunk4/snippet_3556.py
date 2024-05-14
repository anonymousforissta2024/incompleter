#Source: https://stackoverflow.com/questions/63894385/i-keep-getting-the-attributeerror-bot-object-has-no-attribute-fetch-member
class Menu(ListPageSource):
    def __init__(self, ctx, data):
        self.ctx = ctx

        super().__init__(data, per_page=10)

    async def write_page(self, menu, offset, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)

        embed = Embed(title="XP Leaderboard", description="See who is on top!", colour=self.ctx.author.colour)
        embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
        embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} members.")
        
        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)

        return embed

    async def format_page(self, menu, entries):
        offset = (menu.current_page*self.per_page) + 1
        fields = []
        table = ("\n".join(f"{idx+offset}. {self.ctx.bot.fetch_member(entry[0]).display_name} (XP: {entry[1]} | Level {entry[2]})" 
                for idx, entry in enumerate(entries)))

        fields.append(("Ranks", table))

        return await self.write_page(menu, offset, fields)