#Source: https://stackoverflow.com/questions/59905286/nonetype-error-when-trying-to-make-a-custom-beautifulsoup-dagster-type
import requests
from bs4 import BeautifulSoup
from dagster import (
    dagster_type,
    input_hydration_config,
    Selector,
    Field,
    String,
    TypeCheck,
    EventMetadataEntry
)

def max_depth(soup):
    if hasattr(soup, "contents") and soup.contents:
        return max([max_depth(child) for child in soup.contents]) + 1
    else:
        return 0

def html_soup_type_check(value):
    if not isinstance(value, BeautifulSoup):
        return TypeCheck(
            success=False,
            description=(
                'HtmlSoup should be a BeautifulSoup Object, got '
                '{type_}'
            ).format(type_=type(value))
        )

    if not hasattr(soup, "contents"):
        return TypeCheck(
            success=False,
            description=(
                'HtmlSoup has no contents, check that the URL has content'
            )
        )

    return TypeCheck(
        success=True,
        description='HtmlSoup Summary Stats',
        metadata_entries=[
            EventMetadataEntry.text(
                str(max_depth(value)),
                'max_depth',
                'Max Nested Depth of the Page Soup'
            ),
            EventMetadataEntry.text(
                str(set(tag.name for tag in value.find_all())),
                'tag_names',
                'All available tags in the Page Soup'
            )
        ]
    )


@input_hydration_config(
    Selector(
        {
            'url': Field(
                String,
                is_optional=False,
                description=(
                    'URL to be ingested and converted to a Soup Object'
                )
            )
        }
    )
)
def html_soup_input_hydration_config(context, selector):
    url = selector['url']
    res = requests.get(url, params={
        'Content-type': 'text/html'
    })

    if (not res.status_code == 200):
        return TypeCheck(
            success=False,
            description=(
                '{status_code} ERROR, Check that URL: {url} is correct'
            ).format(status_code=res.status_code, url=url)
        )
    soup = BeautifulSoup(res.content, 'html.parser')
    return HtmlSoup(soup)

@dagster_type(
    name='HtmlSoup',
    description=(
        'The HTML extracted from a URL stored in '
        'a BeautifulSoup object.'
    ),
    type_check=html_soup_type_check,
    input_hydration_config=html_soup_input_hydration_config
)
class HtmlSoup(BeautifulSoup):
    pass