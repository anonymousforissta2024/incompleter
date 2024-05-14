#Source: https://stackoverflow.com/questions/45132060/typeerror-using-telnet-write
try:
    tn = Telnet(host, str(port))
except Exception as e:
    print("Connection cannot be established", e)
    traceback.print_exc()
print("You are connected")
tn.write('command?'+'\r\n')
while True:
    line = tn.read_until("\n")