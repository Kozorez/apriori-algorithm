"""
File: apriori.py
Module provides utilities for analysis of transactional database records
in order to find frequent itemsets and derive strong association rules.
"""

def generateFrequentItemset(dataset, min_sup):
	"""
	Generate frequent itemsets from records in dataset.
	Return an item, if its support is greater than min_sup 
	(min_sup must be not greater than number of records in the dataset).
	"""
	
	itemset = {}

	for values in dataset.values():
		for value in values:
			if (value, ) in itemset:
				itemset[value, ] += 1
			else:
				itemset[value, ] = 1

	itemset = _pruneCandidates(itemset, min_sup)

	level = 1
	while itemset:
		previousItemset = itemset

		itemset = _generateCandidates(itemset, level)
		itemset = _computeCandidatesSupport(dataset, itemset)
		itemset = _pruneCandidates(itemset, min_sup)

		level += 1
	else:
		if level > 1:
			itemset = previousItemset

	return itemset

def _generateCandidates(L, k):
	C = {}

	for i in L:
		for j in L:
			if i < j:
				union = set(i) | set(j)
				if len(union) == k + 1:
					union = tuple(sorted(union))
					if _checkAprioriProperty(L, union):
						C[union] = 0

	return C

def _checkAprioriProperty(L, union):
	for i in range(len(union)):
		subset = union[:i] + union[i + 1:]
		if subset not in L:
			return False
	else:
		return True

def _computeCandidatesSupport(dataset, C):
	for i in C:
		for j in dataset.values():
			if set(i) <= set(j):
				C[i] += 1
	
	return C

def _pruneCandidates(C, min_sup):
	res = {}

	for key in C:
		if C[key] >= min_sup:
			res[key] = C[key]

	return res
