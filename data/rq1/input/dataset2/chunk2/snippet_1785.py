#Source: https://stackoverflow.com/questions/74348377/python-selenium-by-raises-attributeerror-type-object-by-has-no-attribute-xpa
def main_test():
    chrome_options = Options()
    prefs = {"download.default_directory": f"{os.getcwd()}/Music"}
    chrome_options.add_argument("user-data-dir=selenium")
    chrome_options.add_experimental_option("prefs", prefs)
    dr = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    dr.get(URL)
    print(f"{selenium.__version__=}")
    dr.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/ul/li[2]/a").click()
    dr.quit()


if __name__ == '__main__':
    main_test()