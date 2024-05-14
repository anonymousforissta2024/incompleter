#Source: https://stackoverflow.com/questions/74394682/why-am-i-getting-this-error-attributeerror-type-object-bubblesort-has-no-att
from random import randint

class bubbleSort:
    def __init__(self, size):
        self.size = size # Array size
        self.array = [] # Random array
        self.sorted = self.array # Sorted array
        self.random = 0 # Random number

        self.count = 0
        self.done = False
        self.equal = 0
        while self.count != self.size:
            random = randint(1, self.size)
            if random in self.array:
                pass
            else:
                self.array.append(random)
                self.count += 1

    def sort(self):
        while self.done != True:
            self.equal = False
            for i in range(self.size):
                if i == self.size:
                    pass
                else:
                    if self.sorted[i] > [self.tmp]:
                        self.equal += 1
                        if self.equal == self.size:
                            self.done = True
                    else:
                        self.sorted[i], self.sorted[i + 1] = self.sorted[i+1], self.sorted[i]


new = bubbleSort(10)
print(bubbleSort.array)