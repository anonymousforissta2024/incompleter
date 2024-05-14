#Source: https://stackoverflow.com/questions/63555043/attributeerror-unknown-cc-while-trying-to-parse-emails-in-ms-outlook-2010-wi
import win32com.client as client

outlook=client.Dispatch('Outlook.Application')

namespace=outlook.GetNameSpace("MAPI")

Der=namespace.Folders['Drive']

Dinbox=Der.Folders['Inbox']

for message in Dinbox.Items:
    if message.Categories =="":
        if "xyz" in message.CC or "xyz" in message.To :
            message.Categories="xyz"