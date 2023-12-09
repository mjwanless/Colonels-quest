from unittest import TestCase

from movement import move_character


class Test(TestCase):
	def test_move_west(self):
		character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 4
		move_character(character, direction)
		actual = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		expected = character
		self.assertEqual(expected, actual)

	def test_move_east(self):
		character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 2
		move_character(character, direction)
		actual = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
		expected = character
		self.assertEqual(expected, actual)

	def test_move_north(self):
		character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
		direction = 1
		move_character(character, direction)
		actual = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		expected = character
		self.assertEqual(expected, actual)

	def test_move_south(self):
		character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 3
		move_character(character, direction)
		actual = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
		expected = character
		self.assertEqual(expected, actual)
