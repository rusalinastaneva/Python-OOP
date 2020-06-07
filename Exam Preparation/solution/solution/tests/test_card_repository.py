from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
import unittest

class TestsCardRepository(unittest.TestCase):
    def test_init_should_create_count_and_cards(self):
        cr = CardRepository()
        self.assertEqual(cr.count, 0)
        self.assertEqual(cr.cards, [])

    def test_add_existing_card_should_raise_error(self):
        cr = CardRepository()
        card = MagicCard("Magic")
        cr.cards.append(card)
        with self.assertRaises(ValueError) as cm:
            cr.add(card)
        self.assertEqual(str(cm.exception), "Card Magic already exists!")

    def test_add_non_existing_card_should_add_it_to_cards(self):
        cr = CardRepository()
        card = MagicCard("Magic") 
        cr.add(card)
        self.assertEqual(cr.cards, [card])

    def test_remove_empty_string_should_raise_error(self):
        cr = CardRepository()
        with self.assertRaises(ValueError) as cm:
            cr.remove("")
        self.assertEqual(str(cm.exception), "Card cannot be an empty string!")

    def test_remove_existing_card_should_remove_it_from_cards(self):
        cr = CardRepository()
        card = MagicCard("Magic") 
        cr.add(card)
        cr.remove("Magic")
        self.assertEqual(cr.cards, [])

    def test_remove_existing_card_should_decrease_count(self):
        cr = CardRepository()
        card = MagicCard("Magic") 
        cr.add(card)
        cr.remove("Magic")
        self.assertEqual(cr.count, 0)

    def test_find_card_by_name_should_return_card(self):
        cr = CardRepository()
        card = MagicCard("Magic") 
        cr.add(card)
        found = cr.find("Magic")
        self.assertEqual(found, card)

if __name__ == "__main__":
    unittest.main()