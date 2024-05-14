#Source: https://stackoverflow.com/questions/76428561/typeerror-webdriver-init-got-multiple-values-for-argument-options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(r'/usr/bin/chromedriver', options=chrome_options)