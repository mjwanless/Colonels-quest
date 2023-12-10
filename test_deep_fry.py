from unittest import TestCase
from unittest.mock import patch

from spells import deep_fry


class Test(TestCase):
	@patch('random.randint', side_effect=[9])
	def test_deep_fry_damage(self, _):
		actual = deep_fry()
		expected = 9
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[5])
	def test_deep_fry_with_different_random_values(self, _):
		actual = deep_fry()
		expected = 5
		self.assertEqual(actual, expected)