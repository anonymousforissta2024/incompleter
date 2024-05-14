#Source: https://stackoverflow.com/questions/37175460/typeerror-post-data-should-be-bytes-or-an-iterable-of-bytes-it-cannot-be-of-ty
#!/usr/bin/env python
#coding: utf-8
userid="NicoNicoCreate@gmail.com"
passwd="********"
import sys, re, cgi, urllib, urllib.request, urllib.error, http.cookiejar, xml.dom.minidom, time, urllib.parse
import simplejson as json

def getToken():
    html = urllib.request.urlopen("http://www.nicovideo.jp/my/mylist").read()
    for line in html.splitlines():
        mo = re.match(r'^\s*NicoAPI\.token = "(?P<token>[\d\w-]+)";\s*',line)
        if mo:
            token = mo.group('token')
            break
    assert token
    return token

def mylist_create(name):
    cmdurl = "http://www.nicovideo.jp/api/mylistgroup/add"
    q = {}
    q['name'] = name.encode("utf-8")
    q['description'] = ""
    q['public'] = 0
    q['default_sort'] = 0
    q['icon_id'] = 0
    q['token'] = token
    cmdurl += "?" + urllib.parse.urlencode(q).encode("utf-8")
    j = json.load( urllib.request.urlopen(cmdurl), encoding='utf-8')
    return j['id']

def addvideo_tomylist(mid,smids):
    for smid in smids:
        cmdurl = "http://www.nicovideo.jp/api/mylist/add"
        q = {}
        q['group_id'] = mid
        q['item_type'] = 0
        q['item_id'] = smid
        q['description'] = u""
        q['token'] = token
        cmdurl += "?" + urllib.parse.urlencode(q).encode("utf-8")
        j = json.load( urllib.request.urlopen(cmdurl), encoding='utf-8')
        time.sleep(0.5)

#Login
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
urllib.request.install_opener(opener)
urllib.request.urlopen("https://secure.nicovideo.jp/secure/login",
                urllib.parse.urlencode( {"mail":userid, "password":passwd}) ).encode("utf-8")
#GetToken
token = getToken()
#MakeMylist&AddMylist
mid = mylist_create(u"Testlist")
addvideo_tomylist(mid, ["sm9","sm1097445", "sm1715919"  ] )