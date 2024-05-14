#Source: https://stackoverflow.com/questions/33323911/why-do-i-get-an-attributeerror-str-object-has-no-attribute-write-in-this
#Testing implementation of writing to file
#save the HTML to a beautiful soup object
soup = BeautifulSoup(browser.page_source, 'html.parser')

#TODO: use breadcrumb of page name for loop later on
breadcrumb = soup.select('.breadcrumb span')
pagename = breadcrumb[0].get_text()

#open a file then write to it
bookPage = os.path.join('books/cpp/VST', pagename+'.txt')
open(pagename, 'wb')
pagename.write(str(soup))

#close file
#pagename.close()


#TODO: move on to next file