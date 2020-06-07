from project.player.player_repository import PlayerRepository
from project.player.advanced import Advanced
from project.card.card_repository import CardRepository
import unittest

class TestsPlayerRepository(unittest.TestCase):
    def test_count_players_are_created_upon_init(self):
        pr = PlayerRepository()
        self.assertEqual(pr.count, 0)
        self.assertEqual(pr.players, [])

    def test_add_existing_player_should_raise_error(self):
        repo = PlayerRepository()
        player = Advanced("Peter")
        repo.players.append(player)
        with self.assertRaises(ValueError) as cm:
            repo.add(player)
        self.assertEqual(str(cm.exception), "Player Peter already exists!")

    def test_add_non_existing_player_should_add_player(self):
        repo = PlayerRepository()
        player = Advanced("Peter")
        repo.add(player)
        self.assertEqual(repo.players, [player])

    def test_add_non_existing_player_should_increase_count(self):
        repo = PlayerRepository()
        player = Advanced("Peter")
        repo.add(player)
        self.assertEqual(repo.count, 1)

    
    def test_remove_empty_string_should_raise_error(self):
        repo = PlayerRepository()
        with self.assertRaises(ValueError) as cm:
            repo.remove("")
        self.assertEqual(str(cm.exception), "Player cannot be an empty string!")

    def test_remove_existing_player_should_remove_him(self):
        repo = PlayerRepository()
        player = Advanced("Peter")
        repo.add(player)
        repo.remove(player.username)
        self.assertEqual(repo.players, [])

    def test_remove_existing_player_should_decrease_count(self):
        repo = PlayerRepository()
        player = Advanced("Peter")
        repo.add(player)
        repo.remove(player.username)
        self.assertEqual(repo.count, 0)

if __name__ == "__main__":
    unittest.main()