#Source: https://stackoverflow.com/questions/47028093/attributeerror-spotify-object-has-no-attribute-current-user-saved-tracks
token = util.prompt_for_user_token(username, scope = scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

sp = spotipy.Spotify(auth = token)

saved = sp.current_user_saved_tracks()
print(saved)
recent = sp.current_user_recently_played()
print(recent)