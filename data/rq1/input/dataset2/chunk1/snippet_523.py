#Source: https://stackoverflow.com/questions/65362791/typeerror-object-of-type-set-is-not-json-serializable-while-using-requests
import requests
headd = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Pragma":"no-cache" ,
    "Accept":"*/*" 
}
content = {
    f"\"_username\":\"MY_EMAIL\",\"_password\":\"MY_PASSWORD\",\"_remember_me\":true" 
}
print(requests.get('https://www.bang.com/login_check',headers=headd,json=content).text)