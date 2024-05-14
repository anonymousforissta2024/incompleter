#Source: https://stackoverflow.com/questions/76895825/pypdf-pdf-merge-typeerror-nonetype-object-is-not-callable
@website.route('/test-pypdf', methods=('GET',))
def test_pypdf():
    with open('document.pdf', 'rb') as inFile, open('overlay.pdf', 'rb') as overlay:
        original = PdfReader(inFile)
        background = original.pages[0]
        print(inFile)
        print(background)
        print(type(background))
        foreground = PdfReader(overlay)
        o = foreground.pages[0]
        print(o)
        print(type(o))

        # merge the first two pages
        background.merge_page(o)

    return 'success'