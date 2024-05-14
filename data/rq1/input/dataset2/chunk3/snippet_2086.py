#Source: https://stackoverflow.com/questions/59853281/attributeerror-set-object-has-no-attribute-timeout
def main():
    url = 'https://www.nur.kz/'
    op = get_html(url)
    take_links = get_links(op)
    start_parse = parse(take_links)


if __name__ == '__main__':
        main()