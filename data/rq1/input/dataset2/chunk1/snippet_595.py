#Source: https://stackoverflow.com/questions/70125758/attributeerror-options-object-has-no-attribute-set-headless
from webbrowser import Chrome
from dolphin.common.commonlogger import CommonLogger
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class FetchMusic:

    def __init__(self):
        print("fetch...")


if __name__ == '__main__':
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
    browser = Chrome(executable_path=r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                     options=opts)
    browser.implicitly_wait(3)
    browser.get('https://ca.finance.yahoo.com/quote/AMZN/profile?p=AMZN')
    results = browser.find_elements_by_xpath('//*[@id="quote-header-info"]/div[3]/div/div/span[1]')
    for result in results:
        print(result.text)