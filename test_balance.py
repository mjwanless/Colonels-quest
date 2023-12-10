from unittest import TestCase

from spells import balance


class Test(TestCase):
    def test_balance_with_max_values(self):
        character = {'Current Mana': 100, 'Max Mana': 100, 'Current HP': 80, 'Max HP': 80}
        balance(character)
        expected_mana = 100
        expected_hp = 80
        self.assertEqual(character['Current Mana'], expected_mana)
        self.assertEqual(character['Current HP'], expected_hp)

    def test_balance_with_exceeded_values(self):
        character = {'Current Mana': 120, 'Max Mana': 100, 'Current HP': 90, 'Max HP': 80}
        balance(character)
        expected_mana = 100
        expected_hp = 80
        self.assertEqual(character['Current Mana'], expected_mana)
        self.assertEqual(character['Current HP'], expected_hp)

    def test_balance_with_values_below_max(self):
        character = {'Current Mana': 50, 'Max Mana': 100, 'Current HP': 60, 'Max HP': 80}
        balance(character)
        expected_mana = 50
        expected_hp = 60
        self.assertEqual(character['Current Mana'], expected_mana)
        self.assertEqual(character['Current HP'], expected_hp)