#Source: https://stackoverflow.com/questions/57024304/how-to-fix-attributeerror-client-object-has-no-attribute-send-message-wit
import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

channel = client.get_channel('CHANNEL ID')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!dfx2'):
        website_url = requests.get('http://novaworld.cc/dfx2lobby.php?lob=pub').text
        soup = BeautifulSoup(website_url, 'html.parser')
        table = soup.find('table')
        test = table.select_one('tr:contains("!GET SOME")')
        text = test.get_text()
        print(text)
        await channel.send(message.channel, content = text)

client.run('TOKEN')