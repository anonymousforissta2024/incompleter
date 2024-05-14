#Source: https://stackoverflow.com/questions/64582633/typeerror-missing-required-positional-arguments-using-getattr
testc.py
class TestClass(object):

    def test(k1, k2, k3, d1):
        print(k1,k2,k3)
        return 'done'