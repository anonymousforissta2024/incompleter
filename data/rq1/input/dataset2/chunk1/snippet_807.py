#Source: https://stackoverflow.com/questions/40287657/load-pickled-object-in-different-file-attribute-error
import utils

class Document(object):
    data = ""

if __name__ == '__main__':
    doc = Document()
    utils.save_document(doc)