from unittest import TestCase
from unittest.mock import patch

from spells import smite


class Test(TestCase):
	def test_smite_with_zero_level(self):
		character = {"Current Level": 0, "Current Mana": 50}
		damage = smite(character)
		self.assertEqual(damage, 0)

	@patch('random.randint', side_effect=[3])
	def test_smite_level_one(self, mock_randint):
		character = {"Current Level": 1, "Current Mana": 50}
		actual = smite(character)
		expected = 3
		mock_randint.assert_called_with(2, 7)
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[3, 2])
	def test_smite_level_two(self, mock_randint):
		character = {"Current Level": 2, "Current Mana": 50}
		actual = smite(character)
		expected = 5
		mock_randint.assert_called_with(2, 7)
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[3, 4, 1])
	def test_smite_level_three(self, mock_randint):
		character = {"Current Level": 3, "Current Mana": 50}
		actual = smite(character)
		expected = 8
		mock_randint.assert_called_with(2, 7)
		self.assertEqual(actual, expected)

	def test_smite_with_negative_level(self):
		character = {"Current Level": -2, "Current Mana": 50}
		damage = smite(character)
		self.assertEqual(damage, 0)
