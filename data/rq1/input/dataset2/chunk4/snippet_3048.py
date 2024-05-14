#Source: https://stackoverflow.com/questions/75357239/python-error-attributeerror-int-object-has-no-attribute-find
contents = soup.find('table').find_all('a')


for i in range(1,52): # <<<<changed
        print("---------------------------")
        link = i.find("td", class_= "cafecoffee").find_all("a")[0]
        print("link :")
        print("naver.com" + link)

        title = i.find("td")
        print("title:",title.text)