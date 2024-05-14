#Source: https://stackoverflow.com/questions/63280083/typeerror-expected-str-bytes-or-os-pathlike-object-not-list-convert
import txt_to_html
import os
path = 'C:\\Users\\Sandy\\PycharmProjects\\untitled1'
text_files = [f for f in os.listdir(path) if f.endswith('.log')]
txt_to_html.parse_txt(text_files)