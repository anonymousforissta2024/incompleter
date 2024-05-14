#Source: https://stackoverflow.com/questions/58958394/typeerror-a-bytes-like-object-is-required-not-str-with-a-mouse-emulation
report = '\x00\x81\x81\x00'
with open('/dev/hidg1', 'rb+') as fd:
    fd.write(report)