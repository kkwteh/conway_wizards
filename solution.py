from __future__ import print_function

from collections import Counter
from operator import mul
from collections import defaultdict


def partition(number):
     answer = set()
     answer.add((number, ))
     for x in range(1, number):
         for y in partition(number - x):
             answer.add(tuple(sorted((x, ) + y)))
     return answer

def possible_ages(number):
    pset = list(partition(number))
    multilengths = set([length for length, count in Counter([len(p) for p in pset]).items() if count >= 2])
    multiprodsums = defaultdict(list)
    for p in pset:
        if len(p) in multilengths:
            multiprodsums[len(p)].append((sum(p), reduce(mul, p, 1)))

    pset = list(partition(number))
    multilengths = set([length for length, count in Counter([len(p) for p in pset]).items() if count >= 2])
    multiprodsums = defaultdict(list)
    for p in pset:
        if len(p) in multilengths:
            multiprodsums[len(p)].append((sum(p), reduce(mul, p, 1)))

    res = set()
    for key, values in multiprodsums.items():
        values_count = Counter(values)
        for tpl, ct in values_count.items():
            if ct > 1:
                res.add(tpl[1])
    return sorted(list(res))

if __name__ == '__main__':
    for i in range(1, 17):
        print(i, possible_ages(i))
