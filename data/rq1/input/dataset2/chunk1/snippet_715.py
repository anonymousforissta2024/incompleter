#Source: https://stackoverflow.com/questions/50021737/detecting-type-errors-using-mypy-without-type-annotations
def foo(x, y):
    print(x[:y])

def main():
    foo('abcde', '2')

if __name__ == "__main__":
    main()