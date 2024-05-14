#Source: https://stackoverflow.com/questions/57750999/want-to-get-text-from-a-div-but-getting-typeerror-str-object-is-not-callable
bs = BeautifulSoup(html, features="lxml")
reg = re.compile(r'u\/\[deleted\]')
main_elt = bs.find("button", {"data-main-id": "vote"})
print(str(main_elt.parent))
vote_div = main_elt.parent.find('div')
print(str(vote_div))
print("vote text:" + vote_div.text())