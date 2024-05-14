#Source: https://stackoverflow.com/questions/34117236/filenotfounderror-errno-2-in-joining-the-file-directories
import requests,os,bs4
# Download the page.
print('Downloading page...')
res=requests.get('https://imgur.com/search?q=cute+dog')
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,"html.parser")

# Find the URL of the image.
comicElem=soup.select('#imagelist img')
for i in range(10):
    comicUrl=comicElem[i].get('src')
    # Download the image.
    print('Downloading image %s...' %(comicUrl))
    res=requests.get('https:'+comicUrl)
    res.raise_for_status()
    # Save the image to f:\\images
    imageFile=open(os.path.join('f:\\image',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()