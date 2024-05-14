#Source: https://stackoverflow.com/questions/70946505/typeerror-when-trying-to-send-outlook-email-via-python
import win32com.client

outlook = win32com.client.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = 'mitchell.mcdonald@veeder.com;mmcdonald1575@gmail.com'
mail.Subject = 'Sample Email'


for i in range(5):
    try:
        mail.send()

    except:
        print("failed")