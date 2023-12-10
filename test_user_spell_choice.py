from unittest import TestCase
from unittest.mock import patch

from combat_logic import user_spell_choice


class Test(TestCase):
    @patch('spells.holy_blast', return_value=10)
    def test_user_spell_choice_holy_blast(self, mock_holy_blast):
        character = {'Current Mana': 50}
        enemy = {'name': 'testChicken', 'Current HP': 50}
        user_choice = 1
        user_spell_choice(character, enemy, user_choice)
        mock_holy_blast.assert_called_once_with(character)
        self.assertEqual(enemy['Current HP'], 40)

    @patch('spells.smite', return_value=15)
    def test_user_spell_choice_smite(self, mock_smite):
        character = {'Current Mana': 50}
        enemy = {'name': 'testChicken', 'Current HP': 50}
        user_choice = 2
        user_spell_choice(character, enemy, user_choice)
        mock_smite.assert_called_once_with(character)
        self.assertEqual(enemy['Current HP'], 35)

    @patch('spells.judgment', return_value=12)
    def test_user_spell_choice_judgment(self, mock_judgment):
        character = {'Current Mana': 50}
        enemy = {'name': 'testChicken', 'Current HP': 50}
        user_choice = 3
        user_spell_choice(character, enemy, user_choice)
        mock_judgment.assert_called_once_with(character)
        self.assertEqual(enemy['Current HP'], 38)

    @patch('spells.heal', return_value=20)
    def test_user_spell_choice_heal(self, mock_heal):
        character = {'Current Mana': 50, 'Current HP': 30, 'Max HP': 50}
        enemy = {'name': 'TestEnemy', 'Current HP': 50}
        user_choice = 4
        user_spell_choice(character, enemy, user_choice)
        mock_heal.assert_called_once_with(character)
        self.assertEqual(character['Current HP'], 50)