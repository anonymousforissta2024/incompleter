#Source: https://stackoverflow.com/questions/75507313/try-exception-typeerror-not-loading-properly
entrada=input("escribe un valor para calcular su raiz: ")
raiz_cuadrada=entrada ** 0.5
try:
    if entrada>=0:
        print(raiz_cuadrada)
    else:
        print("no se puede calcular la raiz cuadrada de un numero negativo")
        raise ValueError
except TypeError:
    #This print below should be showed always as the input is a string always I think
    print("el valor proporcionado no es un número")
    raise TypeError