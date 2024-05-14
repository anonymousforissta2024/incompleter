#Source: https://stackoverflow.com/questions/74023972/i-am-trying-to-run-this-code-and-getting-error-attributeerror-webdriver-objec
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login test pass")
else:
    print("Login test fail")

driver.close()