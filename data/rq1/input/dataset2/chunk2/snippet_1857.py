#Source: https://stackoverflow.com/questions/54897849/circular-issue-attempt-to-send-form-url-encoded-data-causes-typeerror-cant-co
req = Request(url, method='POST', data={"ID": theId})
r = urlopen(req)