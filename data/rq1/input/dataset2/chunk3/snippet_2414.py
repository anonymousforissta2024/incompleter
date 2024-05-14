#Source: https://stackoverflow.com/questions/57262877/urllib-request-urlopen-typeerror-a-bytes-like-object-is-required-not-str
from urllib import request

def get_page(page):
    page = request.urlopen(page).read()
    return page

def get_next_target(page):
    start_link = page.find("<a href=")
    if(start_link == -1):
        return None
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote+1:end_quote]
    print(url)
    return(url,end_quote)

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

page = get_page('https://xkcd.com/')
print(page)
get_next_target(page)
#print_all_links(page)