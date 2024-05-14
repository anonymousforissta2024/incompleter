#Source: https://stackoverflow.com/questions/74576161/selenium-cant-find-a-submit-button-on-login-attributeerror-webdriver-objec
driver.get( 'https://app.quantdata.us/login')

cookies = driver.get_cookies()
driver.implicitly_wait(20)

driver.find_element("id","username").send_keys(username)#works
driver.find_element("id","password").send_keys(password)#works


driver.find_element("id","submit").click() #not working 
driver.findElement("class","submit").click();#notworking
driver.find_element("xpath","//*[@id=__next]/div[1]/div[2]/div[2]/div/form/button").click()#not working
driver.find_element_by_css_selector('button[type=submit]').submit() #not working 
 
driver.find_element("id","submit").click() #not working 
driver.findElement("class","submit").click();#notworking
driver.find_element("xpath","//*[@id=__next]/div[1]/div[2]/div[2]/div/form/button").click()#not working
driver.find_element_by_css_selector('button[type=submit]').submit() #not working 