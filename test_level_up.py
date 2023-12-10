from unittest import TestCase
from combat_logic import level_up


class Test(TestCase):

    def test_level_up_to_level_2(self):
        character = {'Current Level': 1, 'Exp': 30, 'Exp Needed': 20, 'Max HP': 45,
                     'Current HP': 35, 'Max Mana': 75, 'Current Mana': 40}
        level_up(character)
        actual = character
        expected = {'Current HP': 60,
                    'Current Level': 2,
                    'Current Mana': 100,
                    'Exp': 0,
                    'Exp Needed': 40,
                    'Max HP': 60,
                    'Max Mana': 100}
        self.assertEqual(actual, expected)
    def test_level_up_to_level_3(self):
        character = {'Current Level': 2, 'Exp': 15, 'Exp Needed': 35, 'Max HP': 30,
                     'Current HP': 25, 'Max Mana': 50, 'Current Mana': 40}
        level_up(character)
        actual = character
        expected = {'Current HP': 45,
                    'Current Level': 3,
                    'Current Mana': 75,
                    'Exp': 0,
                    'Exp Needed': 55,
                    'Max HP': 45,
                    'Max Mana': 75}
        self.assertEqual(actual, expected)
