#Source: https://stackoverflow.com/questions/67562261/typeerror-a-bytes-like-object-is-required-not-str-what-do-i-change
def convertAudioToByteArray(audio):
    image_data = base64.b64encode(audio).decode('utf-8').encode('ascii')
    return image_data

converted_sound = convertAudioToByteArray(("sounds" + device.get_id() + "/speech" + str(count) + ".mp3"))
payload_json = {'type': 'POLRES', 'img_name':data['img_name'], 'audio': converted_sound, 'node_id': device.get_id()}
payload = json.dumps(payload_json)
device_project_id = args.project_id
device_registry_id = args.registry_id
device_id = data['dev_id']
device_region = args.cloud_region
print("Publishing Polly results to device " + data['dev_id'] + "for image " + data['img_name'])