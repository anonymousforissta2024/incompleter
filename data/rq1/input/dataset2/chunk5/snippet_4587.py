#Source: https://stackoverflow.com/questions/71575913/getting-type-error-typeerror-a-bytes-like-object-is-required-not-str
def escape_characters(message):
    for escape in ESCAPE_TTS_CHARACTERS:
        message = message.replace(escape, "\\"+escape)
    for escape in ESCAPE_EDI_CHARACTERS:
        message = message.replace(escape, "\\"+escape)
    for hexa in HEXA_TTS_CHARACTERS:
        message = message.replace(hexa, "\\x"+ format(ord(hexa), "x"))
    for hexa in HEXA_EDI_CHARACTERS:
        message = message.replace(hexa, "\\x"+ format(ord(hexa), "x"))
    message = message.replace("\x00", "\\x00")
    return message
ESCAPE_TTS_CHARACTERS = ["\\", "{", "}"]
HEXA_TTS_CHARACTERS = ["$", "%"]
ESCAPE_EDI_CHARACTERS = ["'", "*"]
HEXA_EDI_CHARACTERS = ["&", "+", "#", "\"", ":"]    

blob=b'\n\x11\n\x06TmgTty\x10\x00\x1a\x05\n\x03SIM\n\x16\n\x05Event\x10\x00\x1a\x0b\n\tDeparture\n\x12\n\x04Unit\x10\x00\x1a\x08\n\x06Minute\n\x11\n\x05Value\x10\x00\x1a\x06\n\x04-976\n\r\n\x07RefCity\x10\x00\x1a\x00\n\n\n\x04Date\x10\x00\x1a\x00\n\n\n\x04Time\x10\x00\x1a\x00\n\x0c\n\x06DftRul\x10\x00\x1a\x00\n\x0e\n\x05TiaId\x10\x00\x1a\x03\n\x011\n\x10\n\x07LastUid\x10\x00\x1a\x03\n\x011\n\x0b\n\x05Cabin\x10\x00\x1a\x00\n\x0e\n\x08BkgClass\x10\x00\x1a\x00\n\x0c\n\x06TgType\x10\x00\x1a\x00\n\r\n\x07TgValue\x10\x00\x1a\x00'

print(escape_characters(blob))