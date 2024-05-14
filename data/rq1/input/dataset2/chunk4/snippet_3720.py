#Source: https://stackoverflow.com/questions/52414070/attributeerror-nonetype-object-has-no-attribute-mention
client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    channel = client.get_channel("479919577279758340")
    while not client.is_closed:
        loot = random.randint(25,50)
        emojigrab = '💰'
        emojimsg = await client.send_message(channel, emojigrab)
        await client.add_reaction(emojimsg, "👍")
        x = await client.wait_for_reaction(emoji="👍", message=emojimsg,
                                             check=lambda reaction, user: user != client.user)
        if x:
            await client.delete_message(emojimsg)
            await client.send_message(channel, "{} secures the bag. {} found inside. ".format(x.user.mention, loot))
            add_dollars(x.user, loot)
            await asyncio.sleep(1800)

try:
    with open("cash.json") as fp:
        cash = json.load(fp)
except Exception:
    cash = {}

def save_cash():
    with open("cash.json", "w+") as fp:
        json.dump(cash, fp, sort_keys=True, indent=4)

def add_dollars(user: discord.User, dollars: int):
    id = user.id
    if id not in cash:
        cash[id] = {}
    cash[id]["dollars"] = cash[id].get("dollars", 0) + dollars
    print("{} now has {} dollars".format(user.name, cash[id]["dollars"]))
    save_cash()

def remove_dollars(user: discord.User, dollars: int):
    id = user.id
    if id not in cash:
        cash[id] = {}
    cash[id]["dollars"] = cash[id].get("dollars", 0) - dollars
    print("{} now has {} dollars".format(user.name, cash[id]["dollars"]))
    save_cash()

def add_dollars_stolen(user: discord.User, dollars_stolen: int):
    id = user.id
    if id not in cash:
        cash[id] = {}
    cash[id]["dollars_stolen"] = cash[id].get("dollars_stolen", 0) + dollars_stolen
    print("{} stole ${}".format(user.name, cash[id]["dollars_stolen"]))
    save_cash()

def get_dollars_stolen(user: discord.User):
    id = user.id
    if id in cash:
        return cash[id].get("dollars_stolen", 0)
    return 0

def get_dollars(user: discord.User):
    id = user.id
    if id in cash:
        return cash[id].get("dollars", 0)
    return 0

@client.event
async def on_ready():
    print('Bot Online.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("?cash"):
            if message.content.lower() == "?cash":
                if get_dollars(message.author) < 0:
                    await client.send_message(message.channel, "You're ${} in the hole!".format(get_dollars(message.author)))
                else:
                    await client.send_message(message.channel, "You've acquired ${}! :dollar:".format(get_dollars(message.author)))


client.loop.create_task(background_loop())