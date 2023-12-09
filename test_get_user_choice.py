from unittest import TestCase
from unittest.mock import patch
from movement import get_user_choice


class Test(TestCase):
	@patch('builtins.input', side_effect=['1'])
	def test_get_user_choice_valid_input(self, _):
		actual = get_user_choice()
		expected = 1
		self.assertEqual(actual, expected)

	@patch('builtins.input', side_effect=['5', '2'])
	def test_get_user_choice_invalid_then_valid_input(self, _):
		actual = get_user_choice()
		expected = 2
		self.assertEqual(actual, expected)

	@patch('builtins.input', side_effect=['test', '3'])
	def test_get_user_choice_invalid_then_valid_input_with_non_integer(self, _):
		actual = get_user_choice()
		expected = 3
		self.assertEqual(actual, expected)
