#Source: https://stackoverflow.com/questions/72368976/getting-attributeerror-zillowscraper-object-has-no-attribute-items
import requests

class ZillowScraper():
        headers =  {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'zguid=23|%240fe7f848-3c27-4d0b-bb5d-c198cfae3eed; _ga=GA1.2.1801058422.1649112771; zjs_user_id=null; zg_anonymous_id=%2252f46fc8-6a61-480c-98be-cfc562590b04%22; zjs_anonymous_id=%220fe7f848-3c27-4d0b-bb5d-c198cfae3eed%22; _pxvid=f44b59a6-b469-11ec-bbfe-436e5278416e; _gcl_au=1.1.1592676237.1649112771; __pdst=dc3c162684ca4f36a134c8a996a6ec38; _cs_c=0; _fbp=fb.1.1649112771482.2015766220; _pin_unauth=dWlkPU0yRmpaVE5oTldNdFpHUTJOeTAwWXpJd0xXSmhZemN0T0RJek1qVTFaR0ptTlRneg; _gaexp=GAX1.2.oiNeeEqETVWdoXflVRG4Vg.19173.x440; __gads=ID=136d8b8c5f06abc5:T=1649112805:S=ALNI_MYS6-YjMtxivaR1A5Y5cBSVOrrLTA; _hp2_id.1215457233=%7B%22userId%22%3A%228009605281799948%22%2C%22pageviewId%22%3A%226137654812055503%22%2C%22sessionId%22%3A%222835884101545193%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _cs_id=0c0cee1d-528e-a7cc-bc24-2b1930e2b994.1649112771.1.1649116574.1649112771.1.1683276771608; JSESSIONID=976893FBFDB7112B901F17A0E9C0B6B2; zgsession=1|35fd000e-66f1-4675-88d5-b4cb6b7ff097; _gid=GA1.2.405822409.1653242061; pxcts=3638eb14-d9f8-11ec-af64-67794c746154; _px3=ac5166d12159728bf9e5e9f1d7ea9868dc28a2a2b6b2d847fd64b1598e6f133b:veuXNvW0Uw0koU329/12RmY5id1xO5GAuV0HK2c+OW/HrSHQzSqJ8dWzHGYvFI0P86ex4DIvJVkRkrVYib9D9Q==:1000:XCwT6ASwZRs6WeL+uLO1HYeyZiDjkfZjAepxTftjYXYk1hVAzszdYF4sF6FuQJJ/lfsm+KNnt6s9V+7jYBVIEpWufAtYHxBoTOLc52bq6Eg9UUEAJT/IfIpuI173hVdnOedv58+CMZBqOIWO5S0CKaJ/oBpT/2C4wt2yNR0Y6xMxGX5QV0cOeMm4CQ2gSw5q9wNO6Ihlf9nTMze5dxB5qQ==; __gpi=UID=000004466f8d39a3:T=1649114085:RT=1653242077:S=ALNI_MbrPJGbijyYysYOP7aqBX4KNt8NfA; KruxPixel=true; DoubleClickSession=true; _uetsid=3f3d8de0d9f811ecbe4835b2560b871f; _uetvid=f4cf04f0b46911ecac5a09754992c20f; _clck=125wg2g|1|f1o|0; utag_main=v_id:017ff6c7eaf2001e32f40680315205072001706a007e8$_sn:2$_se:1$_ss:1$_st:1653243876731$dc_visit:2$ses_id:1653242076731%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:us-east-1%3Bexp-session$ttd_uuid:90243e32-e8e2-4add-af8c-48302370be65%3Bexp-session; KruxAddition=true; AWSALB=iWL9LuX6lm5nUqBPoePCeJ26dYRjIuvFKcHDlkQulO9YbuTqokS6ik7cSdVqZk8sIqBZrsHvP27FOfPLmA6mdvBelj7JXmmi3rUI0rYUerHpFD37+7Phc48VQzZn; AWSALBCORS=iWL9LuX6lm5nUqBPoePCeJ26dYRjIuvFKcHDlkQulO9YbuTqokS6ik7cSdVqZk8sIqBZrsHvP27FOfPLmA6mdvBelj7JXmmi3rUI0rYUerHpFD37+7Phc48VQzZn; search=6|1655834243587%7Crect%3D40.8356640592369%252C-73.61575888085936%252C40.55975337598839%252C-74.34360311914061%26rid%3D6181%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26lt%3Dfsbo%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%096181%09%09%09%09%09%09; _clsk=1olc19i|1653242242579|5|0|b.clarity.ms/collect',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5'
        }
        def fetch(self, url, params):  
                response = requests.get(url, headers=self, params=params)
                print(response)
                return response

        def run(self):
                url = 'https://www.zillow.com/new-york-ny/fsbo/'
                params = {
                'searchQueryState': '{"pagination":{}, "usersSearchTerm":"New York, NY", "mapBounds":{"west":-74.34360311914061, "east":-73.61575888085936, "south":40.55975337598839,"north":40.8356640592369}, "regionSelection":[{"regionId":6181, "regionType":6}], "isMapVisible":False, "filterState":{"sort":{"value":"globalrelevanceex"}, "fsba":{"value":False}, "nc":{"value":False}, "fore":{"value":False}, "cmsn":{"value":False}, "auc":{"value":False}, "ah":{"value":True}, "isListVisible":True}'}

                res = self.fetch(url, params)

if __name__ == '__main__':
        scraper = ZillowScraper()
        scraper.run()