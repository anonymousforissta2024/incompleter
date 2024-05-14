#Source: https://stackoverflow.com/questions/70837963/name-error-in-class-when-importing-my-script-file-to-another-from
from functools import reduce

class Operators:

    def __init__(self, names):
        
        self.op_name = []

        for name in names:
            self.op_name.append(name)
    
    def __matmul__(self, other):

        if type(other) is Operators:
            
            new_op_list = self.op_name + other.op_name
            
            return Operators(new_op_list)

    def __str__(self):

        return ' @ '.join(map(str, self.op_name))



class Single_Ket:

    def __init__(self, label: tuple, coeff, operator = []):

        self.label = label
        self.coeff = coeff
        self.operators = operator
    
    
    def __str__(self):
        
        Operator_Str = str( eval(' @ '.join(map(str, self.operators))) )
    
        if type(self.label) is tuple:
            
            return '{} * {} @ | {} >'.format(self.coeff, Operator_Str, ', '.join(map(str, self.label)))
        
        else:
            return f'{self.coeff} * {Operator_Str}.|{self.label}>'



if __name__ == '__main__':

    
    Jp = Operators(['Jp'])
    Jm = Operators(['Jm'])


    ket_1 = Single_Ket((1, 1), 1, [Jp @ Jm])

    print(ket_1)