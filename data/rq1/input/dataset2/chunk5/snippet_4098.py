#Source: https://stackoverflow.com/questions/74951298/typeerror-slice-indices-must-be-integers-or-none-or-have-an-index-method-er
import json
import requests
import bs4
from Essentials import Static


class CmsIDs:
    def GetIDs():
        # cont = requests.get(""https://www.facebook.com:443/help"", headers=Static.headers) # syntax error
        cont = requests.get("https://www.facebook.com:443/help", headers=Static.headers)
        soup = bs4.BeautifulSoup(cont.content, "html5lib")

        text = soup.find_all("script")

        start = ""
        txtstr = ""

  

        for i in range(len(text)):
    
            mystr = text[i]

            # mystr = text[i]
            print("this is: ", mystr.find('__bbox":'))
            if text[i].get_text().find('__bbox":') != -1:
                # print(i, text[i].get_text())
                txtstr += text[i].get_text()
                start = text[i].get_text().find('__bbox":') + len('__bbox":')

        print('start:', start)

        count = 0
        for end, char in enumerate(txtstr[start:], start):
            if char == '{':
                count += 1
            if char == '}':
                count -= 1
            if count == 0:
                break
        print('end:', end)

        # --- convert JSON string to Python structure (dict/list) ---

        data = json.loads(txtstr[start:end+1])
        # pp.pprint(data)
        print('--- search ---')
        CmsIDs.search(data)

        # --- use recursion to find all 'cms_object_id', 'cmsID', 'name' ---

    def search(data):
        if isinstance(data, dict):
            found = False
            if 'cms_object_id' in data:
                print('cms_object_id', data['cms_object_id'])
                found = True
            if 'cmsID' in data:
                print('cmsID', data['cmsID'])
                found = True
            if 'name' in data:
                print('name', data['name'])
                found = True
            if found:
                print('---')
            for val in data.values():
                CmsIDs.search(val)
        if isinstance(data, list):
            for val in data:
                CmsIDs.search(val)


if __name__ == '__main__':
    CmsIDs.GetIDs()