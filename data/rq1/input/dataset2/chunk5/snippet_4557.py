#Source: https://stackoverflow.com/questions/55231027/attributeerror-nonetype-object-has-no-attribute-get-text-python-3x
def MainPageSpider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'url' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = bs(plain_text, 'html.parser')
        for link in soup.findAll(attrs={'class':'col4'}):
            href = 'url' + link.a['href']
            title = link.span.text

            PostPageItems(href)
        page += 1


def PostPageItems(post_url):
    source_code = requests.get(post_url)
    plain_text = source_code.text
    soup = bs(plain_text, 'html.parser')
    for items in soup.findAll(attrs={'class':'container'}):
        title2 = items.find('h1', {'class':'title'}).get_text()

        print(title2)




MainPageSpider(1)