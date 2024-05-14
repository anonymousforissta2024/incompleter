#Source: https://stackoverflow.com/questions/71898053/amazon-web-scraping-attributeerror-nonetype-object-has-no-attribute-text
applelist = []

apples = soup.find_all('div', {'class': 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})

for item in apples:
    apple = {
        'title': item.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'}).text,
        'link': 'https://www.amazon.com' + item.find('a', {'class':'a-link-normal s-underline-textjknderline-link-text s-link-style a-text-normal'})['href'],
        'rating': item.find('i', {'class':'a-icon-alt'}).text,
        }
    applelist.append(apple)
    #print(applelist)

df = pd.DataFrame(applelist)
df.to_csv('file.csv')