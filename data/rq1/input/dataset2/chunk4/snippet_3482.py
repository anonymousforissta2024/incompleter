#Source: https://stackoverflow.com/questions/68905652/turbogears2-typeerror-redirect-got-an-unexpected-keyword-argument-pagename
@expose('wiki20.templates.page')
def _default(self, pagename="FrontPage"):
    from sqlalchemy.exc import InvalidRequestError

    try:
        page = DBSession.query(Page).filter_by(pagename=pagename).one()
    except InvalidRequestError:
        raise redirect("notfound", pagename=pagename)

    content = publish_parts(page.data, writer_name="html")["html_body"]
    root = url('/')
    content = wikiwords.sub(r'<a href="%s\1">\1</a>' % root, content)
    return dict(content=content, wikipage=page)