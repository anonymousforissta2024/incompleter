#Source: https://stackoverflow.com/questions/66599287/i-have-already-translated-the-type-into-int-but-still-suffered-a-type-error-pyt
def get_positive_int():
    while True:
        n = int(input("Height: "))
        if n > 0 and n < 9:
            return n
            
def print(n):
    for i in range(n):
        print(" " * (n - i) + "#" * i + " " + "#" * i)
        
def main():
    n = get_positive_int()
    print(n)
    
if __name__ == "__main__":
    main()