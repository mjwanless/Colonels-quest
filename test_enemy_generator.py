from unittest import TestCase
from generators import enemy_generator


class Test(TestCase):
	def test_generate_hen_enemy(self):
		actual = enemy_generator("hen")
		expected = {"name": "hen", "Current HP": 15, "Max HP": 15, "Exp Value": 2}
		self.assertEqual(actual, expected)

	def test_generate_silkie_enemy(self):
		actual = enemy_generator("silkie")
		expected = {"name": "silkie", "Current HP": 30, "Max HP": 30, "Exp Value": 3}
		self.assertEqual(actual, expected)

	def test_generate_rooster_enemy(self):
		actual = enemy_generator("rooster")
		expected = {"name": "rooster", "Current HP": 50, "Max HP": 50, "Exp Value": 5}
		self.assertEqual(actual, expected)

	def test_generate_sanders_enemy(self):
		actual = enemy_generator("sanders")
		expected = {"name": "sanders", "Current HP": 100, "Max HP": 100, "Exp Value": 0}
		self.assertEqual(actual, expected)
