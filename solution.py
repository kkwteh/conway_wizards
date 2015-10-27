from __future__ import print_function

from collections import Counter
from operator import mul

# See http://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
def partition(number):
    """
    Returns a set of integer partitions for the number
    """
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer

def possible_ages(bus_number):
    partitions = list(partition(bus_number))

    # Count the number of partitions that suggest each order pair of
    # (number of kids, wizard's age)
    n_kids_ages = Counter([(len(p), reduce(mul, p, 1)) for p in partitions])

    # If multiple partitions suggest the same number of kids and the same age,
    # add the age to the set of possible ages for the wizard and return the
    # result as a sorted list
    return sorted(list(set([age for (n_kids, age), ct in n_kids_ages.items() if ct > 1])))

if __name__ == '__main__':
    for bus_number in range(1, 20):
        print(bus_number, possible_ages(bus_number))
