from unittest import TestCase
from movement import validate_move


class Test(TestCase):
	def test_validate_moving_north_invalid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 1
		actual = validate_move(board, character, direction)
		expected = False
		self.assertEqual(expected, actual)

	def test_validate_moving_north_valid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
		direction = 1
		actual = validate_move(board, character, direction)
		expected = True
		self.assertEqual(expected, actual)

	def test_validate_moving_west_invalid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 4
		actual = validate_move(board, character, direction)
		expected = False
		self.assertEqual(expected, actual)

	def test_validate_moving_west_valid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 4
		actual = validate_move(board, character, direction)
		expected = True
		self.assertEqual(expected, actual)

	def test_validate_moving_east_invalid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 2
		actual = validate_move(board, character, direction)
		expected = False
		self.assertEqual(expected, actual)

	def test_validate_moving_east_valid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 2
		actual = validate_move(board, character, direction)
		expected = True
		self.assertEqual(expected, actual)

	def test_validate_moving_south_invalid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
		direction = 3
		actual = validate_move(board, character, direction)
		expected = False
		self.assertEqual(expected, actual)

	def test_validate_moving_south_valid(self):
		board = {(0, 0): "You're in room (0, 0); It is empty.", (0, 1): "You're in room (0, 1); It is empty.",
		         (1, 0): "You're in room (1, 0); It is empty.", (1, 1): "You're in room (1, 1); It is empty."}
		character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
		direction = 3
		actual = validate_move(board, character, direction)
		expected = True
		self.assertEqual(expected, actual)
