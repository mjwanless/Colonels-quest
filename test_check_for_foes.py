from unittest import TestCase
from unittest.mock import patch

from game import check_for_foes


class Test(TestCase):
	@patch('random.randint', return_value=1)
	def test_foe_present(self, _):
		actual = check_for_foes()
		expected = True
		self.assertEqual(actual, expected)

	@patch('random.randint', return_value=2)
	def test_no_foe(self, _):
		actual = check_for_foes()
		expected = False
		self.assertEqual(actual, expected)
