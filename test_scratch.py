from unittest import TestCase
from unittest.mock import patch

from spells import scratch


class Test(TestCase):
	@patch('random.choice', return_value=1)
	def test_scratch_lowest_damage(self, _):
		actual_damage = scratch()
		expected_damage = 1
		self.assertEqual(actual_damage, expected_damage)

	@patch('random.choice', return_value=3)
	def test_scratch_with_different_random_value(self, _):
		actual_damage = scratch()
		expected_damage = 3
		self.assertEqual(actual_damage, expected_damage)

	@patch('random.choice', return_value=4)
	def test_scratch_highest_damage(self, _):
		actual_damage = scratch()
		expected_damage = 4
		self.assertEqual(actual_damage, expected_damage)