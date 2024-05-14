#Source: https://stackoverflow.com/questions/46923475/attributeerror-str-object-has-no-attribute-text-printing-css-error
with open('Aperture Science.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        for section in sections:
            try:
                link = section.find_element_by_css_selector("h3 a").get_attribute("href")
                print((section.get_attribute('href')))
            except NoSuchElementException:
                pass
            time.sleep(7)
            try:
                team_name = section.find_element_by_css_selector(".row:nth-child(1) td:nth-child(1)").text
                print(section.text)
            except NoSuchElementException:
                pass
            time.sleep(7)
            try:
                bet = section.find_element_by_css_selector(".odds .odds span").text
                print(bet.text)
            except NoSuchElementException:
                pass
            time.sleep(7)
            writer.writerow((bet, team_name, link))