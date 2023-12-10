from unittest import TestCase
from unittest.mock import patch

from spells import heal


class Test(TestCase):
	@patch('random.randint', side_effect=[5])
	def test_heal_level_1(self, mock_randint):
		character = {'Current Mana': 30, 'Current Level': 1}
		actual = heal(character)
		expected = 5
		mock_randint.assert_called_with(3, 10)
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[8, 7])
	def test_heal_level_2(self, mock_randint):
		character = {'Current Mana': 60, 'Current Level': 2}
		actual = heal(character)
		expected = 15
		mock_randint.assert_called_with(3, 10)
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[8, 6, 7])
	def test_heal_level_3(self, mock_randint):
		character = {'Current Mana': 60, 'Current Level': 3}
		actual = heal(character)
		expected = 21
		mock_randint.assert_called_with(3, 10)
		self.assertEqual(actual, expected)
