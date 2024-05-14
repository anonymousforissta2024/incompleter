#Source: https://stackoverflow.com/questions/71395086/typeerror-expected-string-or-bytes-like-object-when-setting-cookies-gotten-fr
pickle.dump(driver.get_cookies() , open("cookies.pkl","wb")) 