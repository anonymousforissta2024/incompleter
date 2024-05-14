#Source: https://stackoverflow.com/questions/41883486/datatype-mismatch-beautifulsoup-typeerror-unhashable-type-list
jobs_by_city = [
'http://boston.website.org/search/widget',
]

job_kw = [['web site','user', 'account'],['permission', 'name']]
job_kw = sum(job_kw, [])

jobs = []

for job_in_city in jobs_by_city:
    a_job = requests.get(job_in_city)
    soup = BeautifulSoup(a_job.text, "lxml")
    for a in soup.find_all('a', class_="result-title hdrlnk", text=re.compile(job_kw,re.IGNORECASE)):
        print(a.get('href'))
        #jobs.append(a.get('href'))