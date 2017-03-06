import unittest
import apriori
import association

class UnitTest(unittest.TestCase):
	def testFrequentItemsets9(self):
		dataset = {
			"T100": ["I1", "I2", "I5"],
			"T200": ["I2", "I4"],
			"T300": ["I2", "I3"],
			"T400": ["I1", "I2", "I4"],
			"T500": ["I1", "I3"],
			"T600": ["I2", "I3"],
			"T700": ["I1", "I3"],
			"T800": ["I1", "I2", "I3", "I5"],
			"T900": ["I1", "I2", "I3"]
		}
		
		self.assertEqual(apriori.generateFrequentItemset(dataset, 2), {('I1', 'I2', 'I5'): 2, ('I1', 'I2', 'I3'): 2})

	def testFrequentItemsets0(self):
		dataset = {}

		self.assertEqual(apriori.generateFrequentItemset(dataset, 2), {})

	def testFrequentItemsets2(self):
		dataset = {
			"T100": ["I2", "I3"],
			"T200": ["I2", "I3"]
		}

		self.assertEqual(apriori.generateFrequentItemset(dataset, 2), {('I2', 'I3'): 2})

	def testAssociationsFromFrequentItemsets9(self):
		dataset = {
			"T100": ["I1", "I2", "I5"],
			"T200": ["I2", "I4"],
			"T300": ["I2", "I3"],
			"T400": ["I1", "I2", "I4"],
			"T500": ["I1", "I3"],
			"T600": ["I2", "I3"],
			"T700": ["I1", "I3"],
			"T800": ["I1", "I2", "I3", "I5"],
			"T900": ["I1", "I2", "I3"]
		}

		frequentItemsets = apriori.generateFrequentItemset(dataset, 2)
		associationRules = association.generateAssociationRulesFromFrequentItemsets(dataset, frequentItemsets, 70)
		
		self.assertEqual(associationRules, {(('I1', 'I5'), ('I2',)): 1.0, (('I2', 'I5'), ('I1',)): 1.0, (('I5',), ('I1', 'I2')): 1.0})

	def testAssociationsFromFrequentItemsets0(self):
		dataset = {}

		frequentItemsets = apriori.generateFrequentItemset(dataset, 2)
		associationRules = association.generateAssociationRulesFromFrequentItemsets(dataset, frequentItemsets, 70)

		self.assertEqual(associationRules, {})

	def testAssociationsFromFrequentItemsets2(self):
		dataset = {
			"T100": ["I2", "I3"],
			"T200": ["I2", "I3"]
		}

		frequentItemsets = apriori.generateFrequentItemset(dataset, 2)
		associationRules = association.generateAssociationRulesFromFrequentItemsets(dataset, frequentItemsets, 70)

		self.assertEqual(associationRules, {(('I2',), ('I3',)): 1.0, (('I3',), ('I2',)): 1.0})

	def testAssociations9(self):
		dataset = {
			"T100": ["I1", "I2", "I5"],
			"T200": ["I2", "I4"],
			"T300": ["I2", "I3"],
			"T400": ["I1", "I2", "I4"],
			"T500": ["I1", "I3"],
			"T600": ["I2", "I3"],
			"T700": ["I1", "I3"],
			"T800": ["I1", "I2", "I3", "I5"],
			"T900": ["I1", "I2", "I3"]
		}
		
		self.assertEqual(association.generateAssociationRules(dataset, 2, 70), {(('I1', 'I5'), ('I2',)): 1.0, (('I2', 'I5'), ('I1',)): 1.0, (('I5',), ('I1', 'I2')): 1.0})

	def testAssociations0(self):
		dataset = {}

		self.assertEqual(association.generateAssociationRules(dataset, 2, 70), {})

	def testAssociations2(self):
		dataset = {
			"T100": ["I2", "I3"],
			"T200": ["I2", "I3"]
		}

		self.assertEqual(association.generateAssociationRules(dataset, 2, 70), {(('I2',), ('I3',)): 1.0, (('I3',), ('I2',)): 1.0})

unittest.main()
