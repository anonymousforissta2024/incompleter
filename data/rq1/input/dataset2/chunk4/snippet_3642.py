#Source: https://stackoverflow.com/questions/74966994/attributeerror-chatforbidden-object-has-no-attribute-access-hash
# Log in into the telegram account
client = TelegramClient('Tg_scraper', api_id, api_hash)

chats = []
last_date = None
chunk_size = 200
groups = []
hash_list = []

# Get all the groups/channel of the account
result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

# Puts all the group/channel into a list
i = 0
print('Enter a NUMBER to choose a group where the members will be invited into:')
for chat in chats:
    try:
        groups.append(chat)
        hash_list.append(chat.access_hash)
        print(f"({i})" + ' - ' + chat.title)
        i += 1
    except:
        continue

g_index = input("Enter a Number: ")
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)