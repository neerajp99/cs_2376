# # Apriori algorithm

# import itertools for creating iterators for efficient looping
import itertools

# import numpy
import numpy as np
import operator
from collections import defaultdict

# Add min support
min_support = 2
confident = 2

# Reading the data file
with open('retail.txt', "r") as f:
    lines = f.readlines()
f.close()

item_counts = {}

# Find the candidate item
for line in lines:
    line = line.split(',')
    for item in line:
        if item not in item_counts.keys():
            item_counts[item] = 1
        else:
            item_counts[item] += 1

# loop through the items and if it is more than the minimum support, then its frequent
# L(i) is the unwanted sets and C(r) is the candidate itemset
frequent_items = list()
frequent_list = list()
for i in sorted(item_counts):
	# Check if the item is greater than the threshold
	if (item_counts[i] >= min_support):
		# Check if it's not present in the frequent list 
		if i not in frequent_list:
			# Add it to the frequent list
			frequent_items.append(i)
			frequent_list.append(i)

# Creating a new list 
frequent_new_list = list()

while (confident <= len(frequent_list)):
	 # returns r length subsequences of elements from the input iterable
	 for k in itertools.combinations(frequent_list, confident):
	 	for line in lines: 
	 		line=line.split(',')
	 		if k not in item_counts:
	 			item_counts[k] = 0
	 		# Check if it already exists in the previous sets
	 		if set(k).issubset(set(line)):
	 			# If present, increment the value
	 			item_counts[k] += 1

	 for k in itertools.combinations(frequent_list, confident):
	 	if item_counts[k] >= min_support:
	 		frequent_items.append(k)
	 		for ss in k:
	 			if ss not in frequent_new_list:
	 				frequent_new_list.append(ss)


	 frequent_list, frequent_new_list, confident  = frequent_new_list, [], confident + 1
	 


print ("Most frequent sets are: ", frequent_items)





# Previous approach -> manual works till 3rd phase

# item_counts = defaultdict(int)

# # read the dataset
# with open('retail.txt') as f:
#     lines = f.readlines()

# f.close()


# def normalize_group(*args):
#     return str(sorted(args))


# def generate_pairs(*args):
#     pairs = []
#     for i in range(len(args) - 1):
#         for j in range(i + 1, len(args)):
#             pairs.append(normalize_group(args[i], args[j]))
#         return pairs


# # Find the candidate item
# for line in lines:
#     for item in line.split():
#         item_counts[item] += 1

# # loop through the items and if it is more than the minimum support, then its frequent
# frequent_items = set()
# for key in item_counts:
#     if item_counts[key] > min_support:
#         frequent_items.add(key)

# # adding a default dict to keep count of the canidate pairs
# pair_counts = defaultdict(int)

# # doing the second pass on the data
# for line in lines:
#     items = line.split()
#     # print(items)
#     # iterate through the new list with two pointers
#     for i in range(len(items) - 1):
#         # Is the first item frequent, if not then move on
#         if items[i] not in frequent_items:
#             pass
#         # Is the second item frequent, if not then move on
#         for j in range(i + 1, len(items)):
#             if items[j] not in frequent_items:
#                 pass
#             # sort the arguments and stringify them
#             pair = normalize_group(items[i], items[j])
#             pair_counts[pair] += 1


# # frequent pairs
# frequent_pairs = set()
# for key in pair_counts:
#     if pair_counts[key] > min_support:
#         frequent_pairs.add(key)
# # print(frequent_pairs)
# # Third pass
# # find candiate triple
# # adding a default dict to keep count of the canidate pairs
# triple_counts = defaultdict(int)
# for line in lines:
#     items = line.split()

#     # iterate through the new list with two pointers
#     for i in range(len(items) - 2):
#         # Is the first item frequent, if not then move on
#         if items[i] not in frequent_items:
#             pass

#         # Is the second item frequent, if not then move on
#         for j in range(i + 1, len(items) - 1):

#             if items[j] not in frequent_items:
#                 pass

#             first_pair = normalize_group(items[i], items[j])
#             if first_pair not in frequent_items:
#                 pass

#             for k in range(j + 1, len(items)):
#                 if items[k] not in frequent_items:
#                     pass

#                 # Checking for all pairs are frequent or not
#                 pairs = generate_pairs(items[i], items[j], items[k])
#                 if any(pair not in frequent_pairs for pair in pairs):
#                     pass

#                 triple = normalize_group(items[i], items[j], items[k])
#                 triple_counts[triple] += 1
# # frequent triples
# frequent_triples = set()
# for key in triple_counts:
#     if triple_counts[key] > min_support:
#         frequent_triples.add(key)

# triple_counts = {k: v for k, v in triple_counts.items() if v > min_support}
# pair_counts = {k: v for k, v in pair_counts.items() if v > min_support}

# sorted_triples = sorted(triple_counts.items(), key=operator.itemgetter(1))
# sorted_pairs = sorted(pair_counts.items(), key=operator.itemgetter(1))

# for entry in sorted_pairs:
#     print('{0}: {1}'.format(entry[0], entry[1]))

# for entry in sorted_triples:
#     print('{0}: {1}'.format(entry[0], entry[1]))











