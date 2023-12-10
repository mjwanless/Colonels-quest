from unittest import TestCase
from unittest.mock import patch

from spells import flavour_blast


class Test(TestCase):
	@patch('random.randint', side_effect=[1])
	def test_flavour_blast_lowest_damage(self, _):
		actual = flavour_blast()
		expected = 4
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[5])
	def test_flavour_blast_second_lowest_damage(self, _):
		actual = flavour_blast()
		expected = 8
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[10])
	def test_flavour_blast_medium_damage(self, _):
		actual = flavour_blast()
		expected = 10
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[15])
	def test_flavour_blast_high_medium_damage(self, _):
		actual = flavour_blast()
		expected = 12
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[18])
	def test_flavour_blast_high_damage(self, _):
		actual = flavour_blast()
		expected = 15
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[20])
	def test_flavour_blast_highest_damage(self, _):
		actual = flavour_blast()
		expected = 20
		self.assertEqual(actual, expected)
