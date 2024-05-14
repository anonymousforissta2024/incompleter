#Source: https://stackoverflow.com/questions/68084804/typeerror-lambda-takes-1-positional-argument-but-2-were-given-in-simplefix
def decode(self, message: FixMessage, nth: int = 1):
    if (val := message.get(FIELD_ENCRYPT_METHOD, nth)) is not None:
        self.encrypt_method = EncryptMethod(int(val))