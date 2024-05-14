#Source: https://stackoverflow.com/questions/65012433/identifying-location-of-error-typeerror-nonetype-object-is-not-subscriptable
requests.post("http://localhost:5000/todo", 
                  json={"Title":"my first todo", 
                        "Description":"my first todo"})

requests.get("http://localhost:5000/todo", 
                      json={"Title":"my first todo", 
                            "Description":"my first todo"})