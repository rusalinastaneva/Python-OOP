from project.player.beginner import Beginner
from project.card.card_repository import CardRepository
import unittest

class TestBeginner(unittest.TestCase):
    def test_init_player_attributes(self):
        player = Beginner("Peter")
        self.assertEqual(player.card_repository.__class__.__name__, "CardRepository")
        self.assertEqual(player.username, "Peter")
        self.assertEqual(player.health, 50)

    def test_beginner_inherits_player(self):
        self.assertTrue("Player" == Beginner.__bases__[0].__name__)

    def test_set_empty_string_username_should_raise_error(self):
        player = Beginner("Peter")
        with self.assertRaises(ValueError):
            player.username = ""

    def test_set_new_username_should_change_players_username(self):
        player = Beginner("Peter")
        player.username = "George"
        self.assertEqual(player.username, "George")

    def test_set_health_success(self):
        player = Beginner("Peter")
        player.health = 10
        self.assertEqual(player.health, 10)

    def test_is_dead_returns_true(self):
        player = Beginner("Peter")
        player.health = 0
        self.assertTrue(player.is_dead)

    def test_take_negative_damage_should_raise_error(self):
        player = Beginner("Peter")
        with self.assertRaises(ValueError):
            player.take_damage(-20)

    def test_take_positive_damage_should_decrease_health(self):
        player = Beginner("Peter")
        player.take_damage(20)
        self.assertEqual(player.health, 30)

           
if __name__ == "__main__":
    unittest.main()