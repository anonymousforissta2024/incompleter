#Source: https://stackoverflow.com/questions/47968210/python-typeerror-str-object-cannot-be-interpreted-as-an-integer
if current_ins[0] == "REPEAT":
    for i in range(current_ins[1]):
        if last_ins != "":
            instructions.append(last_ins)
            if delay != -1:
                instructions.append(["DELAY", delay])
        else:
            print ("ERROR: REPEAT can't be the first instruction")
            sys.exit(-1)