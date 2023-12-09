from unittest import TestCase
from unittest.mock import patch

from spells import holy_blast


class Test(TestCase):
	def test_holy_blast_with_zero_level(self):
		character = {"Current Level": 0}
		damage = holy_blast(character)
		self.assertEqual(damage, 0)

	@patch('random.randint', side_effect=[3])
	def test_holy_blast_level_one(self, mock_randint):
		character = {"Current Level": 1}
		actual = holy_blast(character)
		expected = 3
		mock_randint.assert_called_with(1, 4)
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[3, 2])
	def test_holy_blast_level_two(self, mock_randint):
		character = {"Current Level": 2}
		actual = holy_blast(character)
		expected = 5
		mock_randint.assert_called_with(1, 4)
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[3, 4, 1])
	def test_holy_blast_level_three(self, mock_randint):
		character = {"Current Level": 3}
		actual = holy_blast(character)
		expected = 8
		mock_randint.assert_called_with(1, 4)
		self.assertEqual(actual, expected)

	def test_holy_blast_with_negative_level(self):
		character = {"Current Level": -2}
		damage = holy_blast(character)
		self.assertEqual(damage, 0)  # The damage should be zero for a character with a negative level
