#Source: https://stackoverflow.com/questions/59946870/with-path-openr-encoding-utf-8-as-file-attributeerror-generator-objec
import pathlib
import functools
import operator
import lxml.etree as etree
from lxml.builder import ElementMaker

ATTRIB = {"xsi": "test.xsd", "xmlns": "http://www.w3.org/2001/XMLSchema-instance"}



def is_element(node):
    return hasattr(node, 'attrib') and 'name' in node.attrib


def create_plural(item):
    pass



def main():
    cwd = pathlib.Path.cwd()
    directories = list(filter(lambda path: path.is_dir(), cwd.iterdir()))
    langs = [path.name for path in directories]
    files = map(operator.methodcaller('glob', '*.xml'), directories)
    #trees = dict.fromkeys(unique_names, dict())


    for path in files:
        with path.open('r', encoding="utf-8") as file:
            tree = etree.parse(file)
        root = tree.getroot()
        name = xml_path.with_suffix('').with_suffix('').name
        out_tree = trees[name]



        for child in filter(is_element, root):
            id = child.attrib['name']
            text = child.text
            if id not in out_tree:
                out_tree[id] = list()
            item = etree.Element('language', attrib={"lang": path.parent.name, "status": "Reviewed"})
            if child.tag == "plurals":
                item.text = create_plural(child)
            else:
                item.text = etree.CDATA(text)
            out_tree[id].append(item)



if __name__ == '__main__':
    main()



    #name = '{}.strings.xml'.format(xml_file.with_suffix('').name)  # name of the file
        #out_p = out_path / lang / name  # path of the output file where it should be located
        #out_p.parent.resolve().mkdir(parents=True, exist_ok=True)  # make directory
        #text = etree.tostring(root, xml_declaration=True, pretty_print=True, encoding="utf-8")
        #with out_p.open('wb') as file:
        #    file.write(text) ```