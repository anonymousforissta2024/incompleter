#Source: https://stackoverflow.com/questions/29587933/attributeerror-module-object-has-no-attribute-choice
import random
from scipy import *
from numpy import linalg as LA
import pickle
import operator


def new_pagerank_step(current_page, N, d, links):
    print(links[current_page])
    if random.rand() > 1 - d:
        next_page = random.choice(links[current_page])
    else:
        next_page = random.randint(0, N)
    return next_page


def pagerank_wikipedia_demo():
    with open("wikilinks.pickle", "rb") as f:
        titles, links = pickle.load(f)
    current_page = 0
    T = 1000
    N = len(titles)
    d = 0.4
    Result = {}
    result = []
    for i in range(T):
        result.append(current_page)
        current_page = new_pagerank_step(current_page, N, d, links)
    for i in range(N):
        result.count(i)
        Result[i] = result.count(i) / T
    Sorted_Result = sorted(Result.items(), key=operator.itemgetter(1))

pagerank_wikipedia_demo()