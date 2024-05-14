#Source: https://stackoverflow.com/questions/56811628/typeerror-generate-input-missing-1-required-positional-argument-n
import sys
from mph.program import Program
from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer

def generate_input(n):
    """
    Returns an alphanumeric string with a length no greater than n.
    """
    fuzzer = AlphaNumericFuzzer(0, n)

    return fuzzer.generate()

if __name__ == '__main__':
    # usage
    if len(sys.argv) != 3:
        print("usage: python3 fuzztut.py num_cases max_length")
        exit(1)

    # command-line arguments    
    num_cases = int(sys.argv[1]) # number of test cases to run
    max_length = int(sys.argv[2]) # maximum length of each string

    results = [] # list for storing the result of each test

    # main loop
    for i in range(num_cases):
        input = generate_input() # generate input string
        return_value = run(input) # run name with our input

        # save test results to our global results list
        test_result = {}
        test_result["num"] = i
        test_result["input"] = input
        test_result["output"] = return_value
        results.append(test_result)

    # print summary
    for test in results:
        print("Case #{:d}:".format(test["num"]))
        print("    IN: " + test["input"])
        print("    OUT: {:4d}".format(test["output"]))
        print("\n")