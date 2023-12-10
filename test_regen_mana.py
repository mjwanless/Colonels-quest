from unittest import TestCase

from spells import regen_mana


class Test(TestCase):

    def test_regen_mana_level_1(self):
        character = {'Current Mana': 20, 'Current Level': 1, 'Max Mana': 50}
        regen_mana(character)
        expected = 29
        actual = character['Current Mana']
        self.assertEqual(actual, expected)

    def test_regen_mana_level_2(self):
        character = {'Current Mana': 20, 'Current Level': 2, 'Max Mana': 75}
        regen_mana(character)
        expected = 31
        actual = character['Current Mana']
        self.assertEqual(actual, expected)

    def test_regen_mana_level_3(self):
        character = {'Current Mana': 20, 'Current Level': 3, 'Max Mana': 70}
        regen_mana(character)
        expected = 33
        actual = character['Current Mana']
        self.assertEqual(actual, expected)