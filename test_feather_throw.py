from unittest import TestCase
from unittest.mock import patch

from spells import feather_throw


class Test(TestCase):
	@patch('random.randint', side_effect=[2, 1, 3])
	def test_feather_throw(self, _):
		expected = 4
		actual = feather_throw()
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[1, 1, 4])
	def test_feather_throw_with_different_random_values(self, _):
		expected = 1
		actual = feather_throw()
		self.assertEqual(actual, expected)