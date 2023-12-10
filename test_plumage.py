from unittest import TestCase
from unittest.mock import patch

from spells import plumage


class Test(TestCase):
	@patch('random.randint', return_value=3)
	def test_plumage_damage(self, _):
		actual = plumage()
		expected = 3
		self.assertEqual(actual, expected)

	@patch('random.randint', return_value=5)
	def test_plumage_with_max_value(self, _):
		actual = plumage()
		expected = 5
		self.assertEqual(actual, expected)

	@patch('random.randint', return_value=1)
	def test_plumage_with_min_value(self, _):
		actual = plumage()
		expected = 1
		self.assertEqual(actual, expected)