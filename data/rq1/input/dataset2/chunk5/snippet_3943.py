#Source: https://stackoverflow.com/questions/52103088/python-error-attributeerror-io-textiowrapper-object-has-no-attribute-in
with open('C:\\temp\\XXX\\names.csv','r') as rf:
    with open('C:\\temp\\XXX\\Testcopyx.csv','w') as wf:
        for line in rf:
            wf.write(line)                
            wf.insert(0, 'New_ID', range(0, 0 + len(wf)))
            # wf
wf.close