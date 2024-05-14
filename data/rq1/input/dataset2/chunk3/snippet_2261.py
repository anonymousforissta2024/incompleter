#Source: https://stackoverflow.com/questions/63520688/typeerror-cant-multiply-sequence-by-non-int-of-type-float-with-multiplying
account_balance = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/main/section/div/div[1]/section[2]/button[1]/span[1]") 
account_balance_value = account_balance.get_attribute("title")  