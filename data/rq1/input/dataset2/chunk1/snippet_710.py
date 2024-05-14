#Source: https://stackoverflow.com/questions/47056068/python-3-6-typeerror-a-bytes-like-object-is-required-not-str-when-trying-to
def get_next_target(page):
    start_link=page.find('<a href=')
    if start_link==-1:
        return None,0
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1,end_quote]
    return url,end_quote

def print_all_links(page):
    while True:
        url,endpos=(get_next_target(page))
        if url:
            print(url)
            page=page[endpos:]
        else:
            break

def get_page(url):
    import urllib.request
    return urllib.request.urlopen(url).read()

print_all_links(get_page('https://youtube.com'))