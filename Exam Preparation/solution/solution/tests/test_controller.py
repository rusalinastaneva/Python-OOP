from project.controller import Controller
from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository
import unittest

class TestsController(unittest.TestCase):
    def test_init_sets_the_correct_attributes(self):
        controller = Controller()
        self.assertEqual(controller.player_repository.__class__.__name__, "PlayerRepository")
        self.assertEqual(controller.card_repository.__class__.__name__, "CardRepository")

    def test_add_beginner_should_add_beginner_to_player_repo(self):
        controller = Controller()
        controller.add_player("Beginner", "Peter")
        player = controller.player_repository.players[0]
        self.assertEqual(player.username, "Peter")
        self.assertEqual(player.__class__.__name__, "Beginner")

    def test_add_advanced_should_add_advanced_to_player_repo(self):
        controller = Controller()
        controller.add_player("Advanced", "Peter")
        player = controller.player_repository.players[0]
        self.assertEqual(player.username, "Peter")
        self.assertEqual(player.__class__.__name__, "Advanced")

    def test_add_player_should_return_message(self):
        controller = Controller()
        message = controller.add_player("Advanced", "Peter")
        self.assertEqual(message, "Successfully added player of type Advanced with username: Peter")


    def test_add_magic_should_add_magic_to_card_repo(self):
        controller = Controller()
        controller.add_card("Magic", "Magic Card")
        card = controller.card_repository.cards[0]
        self.assertEqual(card.name, "Magic Card")
        self.assertEqual(card.__class__.__name__, "MagicCard")

    def test_add_trap_should_add_trap_to_card_repo(self):
        controller = Controller()
        controller.add_card("Trap", "Trap Card")
        card = controller.card_repository.cards[0]
        self.assertEqual(card.name, "Trap Card")
        self.assertEqual(card.__class__.__name__, "TrapCard")

    def test_add_card_should_return_message(self):
        controller = Controller()
        message = controller.add_card("Trap", "Trap Card")
        self.assertEqual(message, "Successfully added card of type TrapCard with name: Trap Card")
    
    def test_add_player_card_should_add_card_to_player_repo(self):
        controller = Controller()
        controller.add_player("Advanced", "Peter")
        controller.add_card("Trap", "Trap Card")
        controller.add_player_card("Peter", "Trap Card")
        card = controller.player_repository.players[0].card_repository.cards[0]
        self.assertEqual(card.name, "Trap Card")

    def test_add_player_card_should_return_message(self):
        controller = Controller()
        controller.add_player("Advanced", "Peter")
        controller.add_card("Trap", "Trap Card")
        message = controller.add_player_card("Peter", "Trap Card")
        self.assertEqual(message, "Successfully added card: Trap Card to user: Peter")

    def test_fight_should_return_message(self):
        controller = Controller()
        controller.add_player("Advanced", "Peter")
        controller.add_player("Advanced", "George")
        controller.add_card("Trap", "Trap Card")
        controller.player_repository.find("Peter").card_repository.add(controller.card_repository.cards[0])
        message = controller.fight("Peter", "George")
        self.assertEqual(message, "Attack user health 255 - Enemy user health 130")
            
    def test_report_returns_correct_str(self):
        controller = Controller()
        controller.add_player("Advanced", "Peter")
        controller.add_player("Advanced", "George")
        controller.add_card("Trap", "Trap Card")
        controller.player_repository.find("Peter").card_repository.add(controller.card_repository.cards[0])
        self.assertEqual(controller.report(), "Username: Peter - Health: 250 - Cards 1\n### Card: Trap Card - Damage: 120\nUsername: George - Health: 250 - Cards 0\n")

if __name__ == "__main__":
    unittest.main()