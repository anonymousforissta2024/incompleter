#Source: https://stackoverflow.com/questions/75408162/for-key-in-keys-typeerror-nonetype-object-is-not-iterable
url = input('\nEnter URL Here: ')
type_url = url.split('?')[0].split('/')[-1]

if type_url == 'tv-guide':
    id_url = url.split('=')[-1]
else:
    id_url = url.split('&')[0].split('=')[-1]

#id_url = url.split('&')[0].split('=')[-1]
#fix_id = id_url.split('=')[-1]
resp = requests.post('https://tvapi-sgn.solocoo.tv/v1/assets/{}/play'.format(id_url), headers=headers, json=json_data).json()
lic_url = resp['drm']['licenseUrl']
mpd_url = resp['url']

print(f'\nMPD URL: {mpd_url}')
print(f'\nLICENSE URL: {lic_url}')

def get_pssh_kid(keyId):
    array_of_bytes = bytearray( b'\x00\x00\x002pssh\x00\x00\x00\x00')
    array_of_bytes.extend(bytes.fromhex("edef8ba979d64acea3c827dcd51d21ed"))
    array_of_bytes.extend(b'\x00\x00\x00\x12\x12\x10')
    array_of_bytes.extend(bytes.fromhex(keyId.replace("-", "")))
    return base64.b64encode(bytes.fromhex(array_of_bytes.hex()))

def get_pssh_mpd(mpd_url):
    r = requests.get(url=mpd_url)
    r.raise_for_status()
    xml = xmltodict.parse(r.text)
    mpd = json.loads(json.dumps(xml))
    tracks = mpd['MPD']['Period']['AdaptationSet']
    for video_tracks in tracks:
        if video_tracks['@mimeType'] == 'video/mp4':
            for t in video_tracks["ContentProtection"]:
                if t['@schemeIdUri'].lower() == "urn:mpeg:dash:mp4protection:2011":
                    kid = t['@cenc:default_KID']
                    pssh = get_pssh_kid(kid)
    return pssh

pssh = get_pssh_mpd(mpd_url).decode('utf-8')

print("\n[green]+ [INFO] PSSH: [/green]" + pssh)

def decrypt_keys():
    wvdecrypt = WvDecrypt(pssh)
    raw_challenge = wvdecrypt.get_challenge()
    challenge_b64 = b64encode(raw_challenge).decode()
    widevine_license = requests.post(
        url=lic_url, data=raw_challenge, headers=headers, timeout=10)
    license_b64 = b64encode(widevine_license.content)
    wvdecrypt.update_license(license_b64)
    keys = wvdecrypt.start_process()
    if keys:
        return keys

keys = decrypt_keys()

for key in keys:
    print("\n[green]+ [INFO] KEY: --key [/green]" + key)