"""
File: association.py
Module provides utilities for generating strong association rules
from frequent itemsets. Uses module apriori to find frequent itemsets
from transactional database.
"""

import apriori

def generateAssociationRulesFromFrequentItemsets(dataset, itemset, min_conf):
	"""
	Generate strong association rules from itemset.
	Return only items, which confidence is greater than argument
	min_conf (min_conf is between 0 and 100).
	"""
	associations = {}
	for item in itemset:
		for subset in _subsets(item):
			if len(subset) > 0 and len(subset) < len(item):
				associations[tuple(sorted(subset)), tuple(sorted(set(item) - set(subset)))] = 0 

	for association in associations:
		left_then_right = 0
		left = 0
		for items in list(dataset.values()):
			if set(association[0]) <= set(items) and set(association[1]) <= set(items):
				left_then_right += 1
			if set(association[0]) <= set(items):
				left += 1

		if left_then_right / left >= min_conf / 100:
			associations[association] = left_then_right / left
		else:
			associations[association] = None
	
	result = {}

	for association in associations:
		if associations[association]:
			result[association] = associations[association]

	return result

def _subsets(item):
    if len(item) > 0:
        head = item[0]
        for tail in _subsets(item[1:]):
            yield (head, ) + tail
            yield tail
    else:
        yield ()

def generateAssociationRules(dataset, min_sup, min_conf):
	"""
	Abstract process of strong association rules mining 
	to include step of frequent itemset mining from dataset.
	Return only items, which support is greater than argument
	min_sup (min_sup <= len(dataset)) 
	and which confidence is greater than argument
	min_conf (min_conf is between 0 and 100).
	"""
	frequentItemsets = apriori.generateFrequentItemset(dataset, min_sup)

	associationRules = generateAssociationRulesFromFrequentItemsets(dataset, frequentItemsets, min_conf)

	return associationRules
