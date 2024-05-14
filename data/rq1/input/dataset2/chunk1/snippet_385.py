#Source: https://stackoverflow.com/questions/63926412/nameerror-name-number-is-not-defined-using-css-selector-as-nth-childn-with
basecss = '#ctl00_ContentPlaceHolder1_Estadocombo > option'
events = self.driver_web_browser.find_elements_by_css_selector(basecss)


for index, val in enumerate(events, 1):
    name = self.driver_web_browser.find_elements_by_css_selector("{}:nth-child({})".format( basecss,index))

    print(index,val.text)

    if self.state == val.text:
        #event = self.driver_web_browser.find_element_by_css_selector(basecss + ("{}:nth-child({})").click())
        click = self.driver_web_browser.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_Estadocombo > option:nth-child('+ index +')').click()
        print(type(click))
        break 