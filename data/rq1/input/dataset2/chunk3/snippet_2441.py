#Source: https://stackoverflow.com/questions/53715464/typeerror-a-bytes-like-object-is-required-not-str-during-oauth-2-0-callbac
authentication_token = request.args['code']
code_payload = {
    "grant_type": "authorization_code",
    "code": str(authentication_token),
    "redirect_uri": REDIRECT_URI
}
encoded_oauth2_tokens = base64.b64encode('{}:{}'.format(CLIENT_ID, CLIENT_SECRET))        
headers = {"Authorization": "Basic {}".format(encoded_oauth2_tokens)}
post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)  