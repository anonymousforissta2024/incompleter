#Source: https://stackoverflow.com/questions/73118140/attributeerror-obj-2-object-has-no-attribute-var-1-getattr
class obj_1:
    def __init__(self):
        self.var_1 = 'Hello'
        self.var_2 = 'World'


    def get_id(self):
        i = self.var_1
        j = self.var_2       
        return i, j

    def vw(self):
        print('Hello..')

class obj_2:
    def __init__(self):
        pass


    def r_data(self):
        print('called r_data')
        x, y = getattr(obj_1, "get_id")(self)

        print('x > ', x)
        print('y > ', y)

    def rd(self):
        getattr(obj_1, 'vw')(self)

if __name__ == '__main__':
    ob = obj_2()
    ob.r_data()