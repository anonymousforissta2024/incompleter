#Source: https://stackoverflow.com/questions/62095650/python-3-x-nameerror
import numpy as np




def coinFlip(p):
    #perform the binomial distribution (returns 1 or 0)
    result = np.random.binomial (1 , p)
    #return flip to be added to numpy array
    return result



'''Main Area'''
#probability of heads vs. tails. this can be changed
p = .5
#num of flips required. this can be changed
n = 10

#initiate array
FullResults = np.arrange(n)

#perform the desired number of flips required probability set above
for i in range(0, n):
    fullResults[i] = coinFlip(p)
    i+=1

#print results
print("probability is set to ", p)
print("Tails = 0, Heads = 1: ", fullResults)
#Total up heads and tails for easy user experience
print("head count: ", np.count_nonzero(fullResults == 1))
print("Tail count: ", np.count_nonzero(fullResults == 0))