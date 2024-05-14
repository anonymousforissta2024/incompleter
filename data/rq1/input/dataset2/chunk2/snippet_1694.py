#Source: https://stackoverflow.com/questions/70308925/getting-error-attributeerror-nonetype-object-has-no-attribute-text
urls = [] 
uni_names = [] 
page_urls_new = [] 
university_details = ["Name","Link","Location","Rank"]

#Determine 
#Colleges 

start_time = int(round(time.time())) 

for i in range(0, len(page_urls)): 
    page_url = page_urls[i] 
    page_text_soup = BeautifulSoup(extract_source(page_url), "lxml") 
    entries = int(page_text_soup.find('strong', attrs={'data-test-id': 'total-items'}).text) 
    entries = int((entries / 20) + (0 if 0 == entries % 20 else 1))