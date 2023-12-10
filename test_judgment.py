from unittest import TestCase
from unittest.mock import patch

from spells import judgment


class Test(TestCase):
	@patch('random.choice', side_effect=[2])
	def test_judgment_level_one(self, mock_choice):
		character = {"Current Mana": 30, "Current Level": 1}
		actual = judgment(character)
		expected = 2
		mock_choice.assert_called_with((0, 2, 4, 6, 8))
		self.assertEqual(actual, expected)

	@patch('random.choice', side_effect=[2, 4])
	def test_judgment_level_two(self, mock_choice):
		character = {"Current Mana": 30, "Current Level": 2}
		actual = judgment(character)
		expected = 6
		mock_choice.assert_called_with((0, 2, 4, 6, 8))
		self.assertEqual(actual, expected)

	@patch('random.choice', side_effect=[0, 8, 4])
	def test_judgment_level_three(self, mock_choice):
		character = {"Current Mana": 60, "Current Level": 3}
		actual = judgment(character)
		expected = 12
		mock_choice.assert_called_with((0, 2, 4, 6, 8))
		self.assertEqual(actual, expected)
