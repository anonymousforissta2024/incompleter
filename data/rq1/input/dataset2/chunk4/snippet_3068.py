#Source: https://stackoverflow.com/questions/65945389/why-am-i-receiving-this-nameerror-when-attempting-to-add-an-outlooks-email-atta
import win32com.client
import datetime as date

# Input
f = open("testfile.txt", "w+")


outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
folder = outlook.Folders.Item("TestFolder")
inbox = folder.Folders.Item("Inbox")
msg = inbox.Items

# Process
list = []

for x in msg:
    senderEmail = x.SenderEmailAddress
    sender = x.SenderName
    subject = x.Subject
    if x.Attachments:
        for f in x.Attachments:
            attachment = f.FileName
    sum = [subject, sender, senderEmail, attachment]
    list.extend(sum)