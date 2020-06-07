from project.battle_field import BattleField
from project.player.beginner import Beginner
from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository
import unittest

class TestsBattleField(unittest.TestCase):
    def test_fight_with_dead_player_should_raise_error(self):
        bf = BattleField()
        p1 = Beginner("Peter")
        p2 = Beginner("George")
        p1.health = 0
        with self.assertRaises(ValueError) as cm:
            bf.fight(p1, p2)
        self.assertEqual(str(cm.exception), "Player is dead!")

    def test_attacker_beginner_should_increase_attributes(self):
        bf = BattleField()
        mg1 = MagicCard("Magic One")
        mg2 = MagicCard("Magic Two")
        p1 = Beginner("Peter")
        p2 = Beginner("George")
        p1.card_repository.add(mg1)
        p1.card_repository.add(mg2)
        bf.fight(p1, p2)
        self.assertEqual(p1.health, 250)

    def test_enemy_beginner_should_increase_attributes(self):
        bf = BattleField()
        p1 = Beginner("Peter")
        p2 = Beginner("George")
        mg1 = MagicCard("Magic One")
        mg2 = MagicCard("Magic Two")
        p2.card_repository.add(mg1)
        p2.card_repository.add(mg2)
        bf.fight(p2, p1)
        self.assertEqual(p2.health, 250)

    def test_player_dies_in_fight(self):
        bf = BattleField()
        mg1 = MagicCard("Magic One")
        mg2 = MagicCard("Magic Two")
        p1 = Beginner("Peter")
        p2 = Beginner("George")
        p1.card_repository.add(mg1)
        p1.card_repository.add(mg2)
        bf.fight(p1, p2)
        with self.assertRaises(ValueError) as cm:
            bf.fight(p1, p2)
        self.assertEqual(str(cm.exception), "Player's health bonus cannot be less than zero.")

if __name__ == "__main__":
    unittest.main()