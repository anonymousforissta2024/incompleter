#Source: https://stackoverflow.com/questions/62740709/typeerror-init-got-an-unexpected-keyword-argument-choices-in-pythons-a
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url',help='Passing one url')
parser.add_argument('-t', '--type', action='store_true',help='To download pages/posts', choices=['pages', 'posts'])
args = parser.parse_args()

url = args.url

if args.type == "pages":
    url_link = url + "/wp-json/wp/v2/pages/?per_page=100"
if args.type == "posts":
    url_link = url + "/wp-json/wp/v2/posts/?per_page=100"