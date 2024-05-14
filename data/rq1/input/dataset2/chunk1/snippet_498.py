#Source: https://stackoverflow.com/questions/59905286/nonetype-error-when-trying-to-make-a-custom-beautifulsoup-dagster-type
@solid
def get_url(context, soup: HtmlSoup):
    return soup.contents