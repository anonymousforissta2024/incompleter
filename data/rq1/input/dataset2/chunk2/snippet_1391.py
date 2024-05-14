#Source: https://stackoverflow.com/questions/67687865/typeerror-can-only-concatenate-str-not-list-to-str-when-using-a-txt-file
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import pyfiglet
from pyfiglet import figlet_format
import colorama
from colorama import Fore, Style

colorama.init()

def title():
    print(figlet_format("Gxzs's Checker!"))
    print(Fore.CYAN + 'Contact me on Discord Gxzs#3448 for Inquiries' + Fore.CYAN)

title()


def check():
    colorama.init()
    token = input("Enter token > ")
    
    username = [line.strip() for line in open("usernames.txt")]
    
    r = requests.get("https://public-ubiservices.ubi.com/v2/profiles?nameOnPlatform=" + username + "&platformType=uplay", headers = {
                'Method':'GET',
                'Authority':'public-ubiservices.ubi.com',
                'Ubi-AppId':'880650b9-35a5-4480-8f32-6a328eaa3aad',
                'Authorization': token,
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Ubi-RequestedPlatformType':'uplay',
                })   
      
    userWasFound = len(r.json()['profiles']) != 0
    for i in range(5):
        print(" ")
    if userWasFound == False:
        print(username + Fore.WHITE + ' is available! :)' + Fore.WHITE)
        with open("available.txt", 'a') as f:
            f.write(f"{username}\n")
            
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/845031037838688297/N8cjHEwfhoYV-kWgSCA8L5vpMP8C32RsuPz29rTawAx7qtXqzlTV5DNuD7cKYPSSkWbw')
        embed = DiscordEmbed(title="Gxzs' Ubisoft Service", description= username + " is available or restricted", color='03b2f8')
        webhook.add_embed(embed)
        embed.set_image(url='https://media2.giphy.com/media/y8fXirTJjj6E0/giphy.gif?cid=ecf05e47foeqh9oalc5del7633idlrw3jg0jp7jo3fs7o8j3&rid=giphy.gif&ct=g')
        response = webhook.execute()
        username="Gxzs' uPlay Bot",
        avatar_url="https://i.4cdn.org/soc/1620674149395.png"

    if userWasFound == True:
        print(username + Fore.WHITE + ' is taken :( ' + Fore.WHITE)

print(Fore.CYAN + "Press ENTER to start the process..." + Fore.CYAN)
input("")
check()