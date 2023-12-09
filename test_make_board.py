from unittest import TestCase

from generators import make_board


class Test(TestCase):
	def test_make_full_board(self):
		actual = make_board()
		expected = {(0, 0): "You're in room (0, 0); There is nothing but fine hardwood under your "
         'feet.',
 (0, 1): "You're in room (0, 1); There is nothing but fine hardwood under your "
         'feet.',
 (0, 2): "You're in room (0, 2); There is nothing but fine hardwood under your "
         'feet.',
 (0, 3): "You're in room (0, 3); There is nothing but fine hardwood under your "
         'feet.',
 (0, 4): "You're in room (0, 4); There is nothing but fine hardwood under your "
         'feet.',
 (0, 6): "You're in room (0, 6);  There is nothing but fine hardwood under "
         'your feet.',
 (0, 7): "You're in room (0, 7);  There is nothing but fine hardwood under "
         'your feet.',
 (0, 8): "You're in room (0, 8);  There is nothing but fine hardwood under "
         'your feet.',
 (0, 9): "You're in room (0, 9);  There is nothing but fine hardwood under "
         'your feet.',
 (0, 10): "You're in room (0, 10);  There is nothing but fine hardwood under "
          'your feet.',
 (0, 12): "You're in room (0, 12);  There is nothing but fine hardwood under "
          'your feet.',
 (0, 13): "You're in room (0, 13);  There is nothing but fine hardwood under "
          'your feet.',
 (0, 14): "You're in room (0, 14);  There is nothing but fine hardwood under "
          'your feet.',
 (0, 15): "You're in room (0, 15);  There is nothing but fine hardwood under "
          'your feet.',
 (0, 16): "You're in room (0, 16);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 0): "You're in room (1, 0); There is nothing but fine hardwood under your "
         'feet.',
 (1, 1): "You're in room (1, 1); There is nothing but fine hardwood under your "
         'feet.',
 (1, 2): "You're in room (1, 2); There is nothing but fine hardwood under your "
         'feet.',
 (1, 3): "You're in room (1, 3); There is nothing but fine hardwood under your "
         'feet.',
 (1, 4): "You're in room (1, 4); There is nothing but fine hardwood under your "
         'feet.',
 (1, 6): "You're in room (1, 6);  There is nothing but fine hardwood under "
         'your feet.',
 (1, 7): "You're in room (1, 7);  There is nothing but fine hardwood under "
         'your feet.',
 (1, 8): "You're in room (1, 8);  There is nothing but fine hardwood under "
         'your feet.',
 (1, 9): "You're in room (1, 9);  There is nothing but fine hardwood under "
         'your feet.',
 (1, 10): "You're in room (1, 10);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 12): "You're in room (1, 12);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 13): "You're in room (1, 13);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 14): "You're in room (1, 14);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 15): "You're in room (1, 15);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 16): "You're in room (1, 16);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 18): "You're in room (1, 18);  There is nothing but fine hardwood under "
          'your feet.',
 (1, 19): "You're in room (1, 19);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 0): "You're in room (2, 0); There is nothing but fine hardwood under your "
         'feet.',
 (2, 1): "You're in room (2, 1); There is nothing but fine hardwood under your "
         'feet.',
 (2, 2): "You're in room (2, 2); There is nothing but fine hardwood under your "
         'feet.',
 (2, 3): "You're in room (2, 3); There is nothing but fine hardwood under your "
         'feet.',
 (2, 4): "You're in room (2, 4): There is a magic barrier here; It resonates "
         'with a power before unknown. It will only open if you are level 2.',
 (2, 5): "You're in room (2, 5): There is a magic barrier here; It resonates "
         'with a power before unknown. It will only open if you are level 2.',
 (2, 6): "You're in room (2, 6);  There is nothing but fine hardwood under "
         'your feet.',
 (2, 7): "You're in room (2, 7);  There is nothing but fine hardwood under "
         'your feet.',
 (2, 8): "You're in room (2, 8);  There is nothing but fine hardwood under "
         'your feet.',
 (2, 9): "You're in room (2, 9);  There is nothing but fine hardwood under "
         'your feet.',
 (2, 10): "You're in room (2, 10): There is a magic barrier here; It resonates "
          'with a power before unknown. It will only open if you are level 3.',
 (2, 11): "You're in room (2, 11): There is a magic barrier here; It resonates "
          'with a power before unknown. It will only open if you are level 3.',
 (2, 12): "You're in room (2, 12);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 13): "You're in room (2, 13);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 14): "You're in room (2, 14);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 15): "You're in room (2, 15);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 16): "You're in room (2, 16);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 17): "You're in room (2, 17): There is a magic barrier here; Beyond "
          'stands Colonel Sanders; Are you ready to complete this quest? '
          'Proceed if so.',
 (2, 18): "You're in room (2, 18);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 19): "You're in room (2, 19);  There is nothing but fine hardwood under "
          'your feet.',
 (2, 20): "You're in room (2, 20)",
 (3, 0): "You're in room (3, 0); There is nothing but fine hardwood under your "
         'feet.',
 (3, 1): "You're in room (3, 1); There is nothing but fine hardwood under your "
         'feet.',
 (3, 2): "You're in room (3, 2); There is nothing but fine hardwood under your "
         'feet.',
 (3, 3): "You're in room (3, 3); There is nothing but fine hardwood under your "
         'feet.',
 (3, 4): "You're in room (3, 4); There is nothing but fine hardwood under your "
         'feet.',
 (3, 6): "You're in room (3, 6);  There is nothing but fine hardwood under "
         'your feet.',
 (3, 7): "You're in room (3, 7);  There is nothing but fine hardwood under "
         'your feet.',
 (3, 8): "You're in room (3, 8);  There is nothing but fine hardwood under "
         'your feet.',
 (3, 9): "You're in room (3, 9);  There is nothing but fine hardwood under "
         'your feet.',
 (3, 10): "You're in room (3, 10);  There is nothing but fine hardwood under "
          'your feet.',
 (3, 12): "You're in room (3, 12);  There is nothing but fine hardwood under "
          'your feet.',
 (3, 13): "You're in room (3, 13);  There is nothing but fine hardwood under "
          'your feet.',
 (3, 14): "You're in room (3, 14);  There is nothing but fine hardwood under "
          'your feet.',
 (3, 15): "You're in room (3, 15);  There is nothing but fine hardwood under "
          'your feet.',
 (3, 16): "You're in room (3, 16);  There is nothing but fine hardwood under "
          'your feet.',
 (3, 18): "You're in room (3, 18);  There is nothing but fine hardwood under "
          'your feet.',
 (3, 19): "You're in room (3, 19);  There is nothing but fine hardwood under "
          'your feet.',
 (4, 0): "You're in room (4, 0); There is nothing but fine hardwood under your "
         'feet.',
 (4, 1): "You're in room (4, 1); There is nothing but fine hardwood under your "
         'feet.',
 (4, 2): "You're in room (4, 2); There is nothing but fine hardwood under your "
         'feet.',
 (4, 3): "You're in room (4, 3); There is nothing but fine hardwood under your "
         'feet.',
 (4, 4): "You're in room (4, 4); There is nothing but fine hardwood under your "
         'feet.',
 (4, 6): "You're in room (4, 6);  There is nothing but fine hardwood under "
         'your feet.',
 (4, 7): "You're in room (4, 7);  There is nothing but fine hardwood under "
         'your feet.',
 (4, 8): "You're in room (4, 8);  There is nothing but fine hardwood under "
         'your feet.',
 (4, 9): "You're in room (4, 9);  There is nothing but fine hardwood under "
         'your feet.',
 (4, 10): "You're in room (4, 10);  There is nothing but fine hardwood under "
          'your feet.',
 (4, 12): "You're in room (4, 12);  There is nothing but fine hardwood under "
          'your feet.',
 (4, 13): "You're in room (4, 13);  There is nothing but fine hardwood under "
          'your feet.',
 (4, 14): "You're in room (4, 14);  There is nothing but fine hardwood under "
          'your feet.',
 (4, 15): "You're in room (4, 15);  There is nothing but fine hardwood under "
          'your feet.',
 (4, 16): "You're in room (4, 16);  There is nothing but fine hardwood under "
          'your feet.'}
		self.assertEqual(actual, expected)
