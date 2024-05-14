#Source: https://stackoverflow.com/questions/74565149/global-variable-doesnt-work-how-do-i-get-the-same-exact-value-of-a-variable-ou
def validate_pnr(ips):
    sum_odd = 0
    sum_even = 0
    total = 0 
    #global diva
    ips = ips.replace("-", "")
    ips = ips.replace(" ", "")
    ips = ips[::-1]
    
    for digit in ips[::2]:
        sum_odd += int(digit)

    for digit in ips[1::2]:
        digit = int(digit) * 2
        if digit >= 10:
            sum_even += (1+(digit % 10))
        else:
            sum_even += digit

    total = sum_odd + sum_even
    divide = total % 10 == 0
    diva = divide
 
    return diva and ips


if __name__ == "__main__":

    print("Welcome to National Provider Identifier numbers (NPI) validator")
    print("Write in the format (YYMMDD-NNNN):")
    answer= input("You want to try? (Y/N): ")

    while answer != "N":
        ips = input("Write in the format (YYMMDD-NNNN): ")
        while diva == True:  #Here I get the error
            validate_pnr(ips)
            answer = input("You want to try another one? (Y/N): ")
            if answer == "N":
                print("Program is executing...")






    