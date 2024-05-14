#Source: https://stackoverflow.com/questions/42930366/how-to-remove-typeerror-in-robobrowser
url = 'http://xx.yy.zz.abc:defg/opac/html/checkouts'  
browser = RoboBrowser(history=False ,parser='lxml')  
browser.open(url=url)  

sign_up = browser.get_form(action='./memberlogin')
sign_up['txtmemberid'].value = 'user-id'
opens = browser.submit_form(sign_up)
print(opens.parsed)