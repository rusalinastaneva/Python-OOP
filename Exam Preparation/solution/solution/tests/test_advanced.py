from project.player.advanced import Advanced
from project.card.card_repository import CardRepository
import unittest

class TestAdvaced(unittest.TestCase):
    def test_init_player_attributes(self):
        player = Advanced("Peter")
        self.assertEqual(player.card_repository.__class__.__name__, "CardRepository")
        self.assertEqual(player.username, "Peter")
        self.assertEqual(player.health, 250)

    def test_beginner_inherits_player(self):
        self.assertTrue("Player" == Advanced.__bases__[0].__name__)

    
if __name__ == "__main__":
    unittest.main()