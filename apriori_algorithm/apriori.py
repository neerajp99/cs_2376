# Apriori algorithm

# import itertools for creating iterators for efficient looping
import itertools

# import numpy
import numpy as np
import operator
from collections import defaultdict

# Add min support
min_support = 5

item_counts = defaultdict(int)

# read the dataset
with open('retail.txt') as f:
    lines = f.readlines()

f.close()


def normalize_group(*args):
    return str(sorted(args))


def generate_pairs(*args):
    pairs = []
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            pairs.append(normalize_group(args[i], args[j]))
        return pairs


# Find the candidate item
for line in lines:
    for item in line.split():
        item_counts[item] += 1

# loop through the items and if it is more than the minimum support, then its frequent
frequent_items = set()
for key in item_counts:
    if item_counts[key] > min_support:
        frequent_items.add(key)

# adding a default dict to keep count of the canidate pairs
pair_counts = defaultdict(int)

# doing the second pass on the data
for line in lines:
    items = line.split()
    # print(items)
    # iterate through the new list with two pointers
    for i in range(len(items) - 1):
        # Is the first item frequent, if not then move on
        if items[i] not in frequent_items:
            pass
        # Is the second item frequent, if not then move on
        for j in range(i + 1, len(items)):
            if items[j] not in frequent_items:
                pass
            # sort the arguments and stringify them
            pair = normalize_group(items[i], items[j])
            pair_counts[pair] += 1

# frequent pairs
frequent_pairs = set()
for key in pair_counts:
    if pair_counts[key] > min_support:
        frequent_pairs.add(key)


pair_counts = {k: v for k, v in pair_counts.items() if v > min_support}
sorted_pairs = sorted(pair_counts.items(), key=operator.itemgetter(1))

for entry in sorted_pairs:
    print('{0}: {1}'.format(entry[0], entry[1]))
