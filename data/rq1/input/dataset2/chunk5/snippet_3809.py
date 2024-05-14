#Source: https://stackoverflow.com/questions/60092328/conecting-to-rest-api-with-python-typeerror-dict-object-is-not-callable
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parametros = {"type" : "isodistance",
              "value" : 10000,
              "lat" : 43.334098,
              "lng" : -1.7920697,
              "approx" : 1000,
              "mobility" : "motor_vehicle",
              "speedType" : "normal",
              "reduceQueue" : "false",
              "avoidTolls" : "true",
              "restrictedAreas" : "false",
              "fastestRouting" : "true",
              "concavity" : 6,
              "buffering" : 3,
              "reqId" : "A57X"}

respuesta = request.GET("http://www.iso4app.net/rest/1.3/isoline.geojson?licKey=4ECDEFB8-1F48-4A0B-A5CA-5B0420162922", parametros)