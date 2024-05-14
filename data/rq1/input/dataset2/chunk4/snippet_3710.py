#Source: https://stackoverflow.com/questions/59883883/dont-understand-why-this-nameerror-name-null-is-not-defined-exception-occurs
data = [{"id": 111,
         "description": "",
         "name": null,
         "name_with_namespace": "Zzzz",
         "path": "Zzzz"
         },
        {"id": 222,
         "description": "",
         "name": "xp-demo-gradle",
         "name_with_namespace": "xp-demo-gradle",
         "path": "xp-demo-gradle"
         }]
for request in data:
    lista = []
    request["id"]
    paragraph = "id: " + str(request["id"]) + "; Path: " + request["path"] + "; Name: " + request["name"]
    artifact = {
        "requested_by": "RequestFetcher",
        "argument": {
            "topic": {
                "id": 2
                },
            "key": str(request["id"]),
            "title": "ID " + str(request["id"]),
            "text": paragraph,
            "cached": True,
            "_links": [
                {
                    "href": "https://gitlab.local.com/api/v4/projects/" + str(request["name"]),
                    "rel": "self",
                    "method": "GET"
                    }
                ],
            }
        }
    lista.append(artifact)
    print(lista)