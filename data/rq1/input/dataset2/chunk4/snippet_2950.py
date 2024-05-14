#Source: https://stackoverflow.com/questions/65008891/typeerror-object-of-type-httpconnection-has-no-len-in-python-3-7
import bs4 as bs
import streamlit as st

source_txt = st.text_input("") #Input url will be entered, say: https://rgtnt.com/
st.write(source_txt)

import http
source = http.client.HTTPConnection(source_txt)

page_soup = bs.BeautifulSoup(source, 'html.parser')