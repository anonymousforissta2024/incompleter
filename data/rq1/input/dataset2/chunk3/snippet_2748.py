#Source: https://stackoverflow.com/questions/60127532/no-matter-what-i-do-i-keep-getting-attributeerror-str-object-has-no-attribute
ajax_data = json.load(request.data.read().decode('utf-8')) 
ajax_data = json.loads(request.data.read().decode('utf-8'))
ajax_data = json.loads(request.data.read())
ajax_data = json.load(request.data.read())
ajax_data = json.load(request.data.decode())
ajax_data = json.loads(request.data.decode())