#Source: https://stackoverflow.com/questions/65100753/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-only-whe
import re
from inspect import Parameter
def get_args(f):
    args = list()
    kwargs = dict()
    for param in inspect.signature(f).parameters.values():
        if (param.kind == param.POSITIONAL_OR_KEYWORD):
            if param.default ==Parameter.empty:
                args.append(param.name)
            else:
                kwargs[param.name]= param.default 
    return args, kwargs 

def  compileKwargs(dct):
    string =""
    poke = False
    for k, o  in dct.items():
        if type(o) == str:
            string+= k+"='"+o+"', "
        else:           
            string+= k+"="+str(o)+", "

    return string

def  compileKwargs2(dct):
    string =""
    poke = False
    for k, o  in dct.items():
        if type(o) == str:
            string+= k+"='"+k+"', "
        else:           
            string+= k+"="+k+", "

    return string

def stringArgs(liste):
    return " ".join([e+"," for e in liste])

def compileArgs(liste1,liste2):
    liste1.extend([e for e in liste2 if e not in liste1])
    return liste1

def editFuncName(actual: str, replace:str):
    #print('EDITFUNCNAME')
    #print(actual)
    string = re.sub('(?<=def ).*?(?=\()',replace, actual)
    #print('string', string)
    return string

import inspect
from textwrap import dedent, indent
def processCode(code : list):
    string=""
    #print('processcode')
    for i,e  in enumerate(code):
        #print('row', e)
        #print('dedent', e)
        if i != 0:
            string+=indent(dedent(e),'\t')
        else :
            string+=dedent(e)
    return string
import types
class MagicMeta(type):
    def __init__(cls, name, bases, dct):
        #print(bases,dct)
        setattr(cls,'_CODE_', dict())

        #GET THE __init__ code function and its arg and kwargs
        # for the class and the inherited class
        func = cls.__init__
        cls._CODE_[func.__name__]= inspect.getsourcelines(func)
        args2 =get_args(cls.__bases__[0].__init__)
        
        setattr(cls,'_ARGS_', dict())
        cls._ARGS_[func.__name__]=[get_args(func), args2]

        lines = cls._CODE_['__init__']
        string= lines[0][0]
        arg, kwarg = cls._ARGS_['__init__'][0]
        arg2, kwarg2 = cls._ARGS_['__init__'][1]

        comparg = stringArgs(compileArgs(arg, arg2))
        #------------------------------------------------------

        #PROCESS arg and kwargs to manage it as string
        dct = {**kwarg ,**kwarg2}
        #print(dct)
        newargs = comparg + compileKwargs(dct)
        string = re.sub('(?<=\().*?(?=\))',newargs, string)
        print(type(arg2))
        print(arg2)
        superarg =stringArgs([a for a in arg2 if a != 'self']) + compileKwargs2(kwarg2)
        arg =stringArgs([a for a in arg2 if a != 'self'])
        printt = "print({})\n".format(arg)
        printtt = "print(locals())\n"
        print(superarg)
        #--------------------------------------------------------

        #ADD the super().__init__ in the __init__ function
        superx = "super({},self).{}({})\n".format(cls.__name__, func.__name__, superarg)
        #superx = "super().{}({})\n".format( func.__name__, superarg)
        print(superx)
        code = lines[0]
        #print('LINE DEF', code[0])
        #--------------------------------------------------------

        #BUILD the code of the new __init__ function
        code[0]= editFuncName(string, 'tempo')
        code.insert(1, printt)
        code.insert(2, "print(self, type(self))\n")
        if len(bases)>0:
            code.insert(3, superx)
 
        print('code:',code)
        codestr  = processCode(code)
        #print('précompile', codestr)
        #--------------------------------------------------------

        #REPLACE the __init__ function code
        comp = compile(codestr, '<string>','exec')
        #print(comp)
        exec(comp)
        cls.__init__ = types.MethodType(eval('tempo'), cls)
        #print(eval('tempo.__code__'))
        #--------------------------------------------------------