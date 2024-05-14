#Source: https://stackoverflow.com/questions/38931066/typeerror-string-indices-must-be-integer
api.authenticate(LOGIN, CONN)
profil = api.get_profile("abc")
data = json.dumps(profil, indent=4)
print(data["login"])