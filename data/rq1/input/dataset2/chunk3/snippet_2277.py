#Source: https://stackoverflow.com/questions/58891720/how-to-fix-this-error-in-selenium-attributeerror-list-object-has-no-attribut
for s in site:
    time.sleep(3)
    URL = 'https://www.bing.com/search?q=site%3a' + str(site) + '&qs=n&sp=-1&pq=site%3a' + str(site) + '&sc=0-22&sk=&cvid=D38F613A00C64A88B2C0F87BD653088A&first=' + str(url_p)     
    driver.get(URL)

    title = driver.find_elements_by_tag_name('h2')
    link = driver.find_elements_by_tag_name('h2')
    link.find_elements_by_css_selector('a').get_attribute('href')