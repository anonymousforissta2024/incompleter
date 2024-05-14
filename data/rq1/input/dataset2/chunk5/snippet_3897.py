#Source: https://stackoverflow.com/questions/60661533/type-error-function-missing-1-required-positional-argument-s
class Solution:
    def lengthOfLongestSubstring(self, s):
        arr = [char1 for char1 in s]
        help_arr = [i*0 for i in range(26)]
        sub_strings = []
        sub = ""
        for char in s:
            index = ord(char) - ord('a')
            if help_arr[index] == 0:
                help_arr[index] = int(1)
                sub += char
            else:
                sub_strings.append(sub)
                sub = ""
                sub += char
                help_arr = [i * 0 for i in range(26)]
                help_arr[index] = int(1)
        max(sub_strings)


    def max(arr):
        max = 0
        index = -1
        for i in range(len(arr)):
            if len(arr[i]) > max:
                max = len(arr[i])
                index=  i
        return print("The answer is '{}', with the length of {}.".format(arr[index], max))

    #call to function
    lengthOfLongestSubstring("aabcdefffgges")