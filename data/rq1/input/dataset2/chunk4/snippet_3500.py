#Source: https://stackoverflow.com/questions/74811176/range-function-argument-returning-typeerror-not-all-arguments-converted-during
for number in my_list:
    if number%3 ==0 and number%5 ==0:
        my_list[number] = "FizzBuzz"
    elif number%3 == 0:       
        my_list[number] = "Fizz"
    elif number%5 == 0:
        my_list[number] ="Buzz"
    
print(my_list)