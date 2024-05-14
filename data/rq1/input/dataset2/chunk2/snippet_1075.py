#Source: https://stackoverflow.com/questions/52342233/python-3-x-python-exec-function-throws-typeerror-for-no-reason
def parse(input_var):
    input_var = input_var.split("[METHOD]")
    if(len(input_var)>1):
        input_var[0] = input_var[0].replace("using ","exec(parse(")
        input_var[0] = input_var[0].replace(";","))")
        input_var = input_var[0]+input_var[1]
    else:
        input_var=input_var[0]
    exec(input_var)


foo="""
using bar;
[METHOD]
print('Passed foo!')
"""

bar = """
print('Passed bar!')
"""

parse(foo)