#Source: https://stackoverflow.com/questions/71014901/attributeerror-nonetype-object-has-no-attribute-get-member
class Rostercheck(commands.Cog, name='Rostercheck'):
    def __init__(self, bot):
        self.bot = bot
        self.roster = {
            "sast" : {"roster": "PLACEHOLDER", "discordid_range":'PLACEHOLDER'}
        }   
        self.guild_metadata = {"sast": PLACEHOLDER}
        self.channel_metadata = {
            "sast": {"roster_check": PLACEHOLDER}
        }
        self.check_discord_members.start()

    async def send_message(self, content, channel=None):
        try:
            await channel.send(content)
        except Exception as e:
            print(f"Encountered exception: {e}")

    async def get_roster_sheet(self, dept_name):
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        service_account_file = './keys.json'
        creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
        service = build('sheets', 'v4', credentials=creds)
        my_dept_roster = self.roster.get(dept_name)
        sheet = service.spreadsheets()
        return sheet.values().get(spreadsheetId=my_dept_roster.get("roster"),range=my_dept_roster.get("discordid_range")).execute()

    @tasks.loop(seconds=100)
    async def check_discord_members(self):
        print("yo")
        for dept_name in self.roster.keys():
            print(dept_name)
            google_sheet = await self.get_roster_sheet(dept_name)
            print(google_sheet)
            for value_list in google_sheet.get("values"):
                print(value_list)
                if len(value_list) != 1 or value_list is None or "Discord ID" in value_list:
                    continue
                value = value_list[0]
                print(value)
                discord_server = self.bot.get_guild(self.guild_metadata.get(dept_name))
                print(discord_server)
                discord_member = discord_server.get_member(int(re.sub("[^0-9]", "", value)))
                print(discord_member)
                if discord_member is None:
                    my_chan = self.bot.get_channel(id=self.channel_metadata.get(dept_name).get("roster_check"))
                    print(my_chan)
                    await self.send_message(f"{value} - <@{value}> is not within the {dept_name} roster, are you sure they are still in your department?", my_chan)  

def setup(bot):
    bot.add_cog(Rostercheck(bot))