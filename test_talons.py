from unittest import TestCase
from unittest.mock import patch

from spells import talons


class Test(TestCase):
	@patch('random.choice', side_effect=[2, 4, 6])
	def test_talons_damage(self, _):
		actual = talons()
		expected = 12
		self.assertEqual(actual, expected)

	@patch('random.choice', side_effect=[5, 3, 4])
	def test_talons_with_different_random_values(self, _):
		actual = talons()
		expected = 12
		self.assertEqual(actual, expected)
