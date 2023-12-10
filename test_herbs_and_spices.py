from unittest import TestCase
from unittest.mock import patch

from spells import herbs_and_spices


class Test(TestCase):
	@patch('random.randint', side_effect=[1] * 11)
	def test_herbs_and_spices_damage(self, _):
		actual = herbs_and_spices()
		expected = 11
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[2] * 11)
	def test_herbs_and_spices_with_different_random_values(self, _):
		actual = herbs_and_spices()
		expected = 22
		self.assertEqual(actual, expected)

	@patch('random.randint', side_effect=[0] * 11)
	def test_herbs_and_spices_no_damage(self, _):
		actual = herbs_and_spices()
		expected = 0
		self.assertEqual(actual, expected)
