#Source: https://stackoverflow.com/questions/63554221/typeerror-object-of-type-bytes-is-not-json-serializable-python-3-try-to-pos
dict_data: dict = {
  'img': base64.b64encode(urlopen(obj['recognition_image_path']).read())
}
json_data: str = json.dumps(dict_data)