from unittest import TestCase

from spells import post_fight_heal


class Test(TestCase):
	def test_post_fight_heal_with_fixed_values(self):
		character = {'Current Mana': 20, 'Current HP': 30, "Max Mana": 80, "Max HP": 80}
		post_fight_heal(character)
		expected_mana = 30
		expected_hp = 35
		self.assertEqual(character['Current Mana'], expected_mana)
		self.assertEqual(character['Current HP'], expected_hp)

	def test_post_fight_heal_with_different_random_values(self):
		character = {'Current Mana': 45, 'Current HP': 25, "Max Mana": 80, "Max HP": 80}
		post_fight_heal(character)
		expected_mana = 55
		expected_hp = 30
		self.assertEqual(character['Current Mana'], expected_mana)
		self.assertEqual(character['Current HP'], expected_hp)

	def test_post_fight_heal_with_too_much_health(self):
		character = {'Current Mana': 80, 'Current HP': 80, "Max Mana": 80, "Max HP": 80}
		post_fight_heal(character)
		expected_mana = 80
		expected_hp = 80
		self.assertEqual(character['Current Mana'], expected_mana)
		self.assertEqual(character['Current HP'], expected_hp)
