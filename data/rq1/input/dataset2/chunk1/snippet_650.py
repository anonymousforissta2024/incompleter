#Source: https://stackoverflow.com/questions/35200142/typeerror-with-html-escaping-in-python3
from html import escape
project_name_unescaped = Project.get('name').encode('utf-8')
project_name = escape(project_name_unescaped)