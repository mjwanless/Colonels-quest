from unittest import TestCase
from unittest.mock import patch

from spells import peck


class Test(TestCase):
	@patch('random.choice', return_value=2)
	def test_peck_lowest_damage(self, _):
		actual_damage = peck()
		expected_damage = 2
		self.assertEqual(actual_damage, expected_damage)

	@patch('random.choice', return_value=4)
	def test_peck_with_different_random_value(self, _):
		actual_damage = peck()
		expected_damage = 4
		self.assertEqual(actual_damage, expected_damage)

	@patch('random.choice', return_value=6)
	def test_peck_highest_damage(self, _):
		actual_damage = peck()
		expected_damage = 6
		self.assertEqual(actual_damage, expected_damage)
