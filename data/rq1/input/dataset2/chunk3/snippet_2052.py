#Source: https://stackoverflow.com/questions/63703233/getting-typeerror-must-be-str-not-bytes-with-echo-command
"echo \"" + base64.b64encode(b'Hello World') + "\" | base64 -d"