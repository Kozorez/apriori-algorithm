"""
File: apriori.py
Module provides utilities for analysis of transactional database records
in order to find frequent itemsets and derived strong association rules.
"""

def generateFrequentItemset(dataset, min_sup):
	"""
	Generate frequent itemsets from record in dataset.
	Return only items, which support is greater than argument
	min_sup (min_sup is less than dataset length).
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
		prevItemset = itemset

		itemset = _generateCandidates(itemset, level)
		itemset = _scanDataset(dataset, itemset)
		itemset = _pruneCandidates(itemset, min_sup)

		level += 1
	else:
		if level > 1:
			itemset = prevItemset

	result = {}
	
	for item in itemset:
		result[item] = itemset[item]

	return result

def _generateCandidates(L, k):
	C = {}
	for i in L:
		for j in L:
			if i < j:
				union = set(i) | set(j)
				if len(union) == k + 1:
					union = tuple(sorted(union))
					if _check(L, union):
						C[union] = 0

	return C

def _check(L, union):
	for i in range(len(union)):
		subset = union[:i] + union[i + 1:]
		if subset not in L:
			return False
	else:
		return True

def _scanDataset(dataset, C):
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
