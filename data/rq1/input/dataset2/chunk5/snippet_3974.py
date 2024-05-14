#Source: https://stackoverflow.com/questions/53863349/error-while-executing-a-rest-api-script-in-python-typeerrordict-object-is-n
req = request.POST('https://graph.microsoft.com/beta/teams')
headers = {'content-type': 'application/json'}
payload = {
'template@odata.bind': 
'https://graph.microsoft.com/beta/teamsTemplates/standard',
'displayName': 'My Sample Team',
'description': 'My Sample Team’s Description',
}