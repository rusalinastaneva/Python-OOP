from project.card.magic_card import MagicCard
import unittest

class TestsMagicCard(unittest.TestCase):
    def test_init_should_create_all_attributes(self):
        mg  = MagicCard("It's some kind of magic...")
        self.assertEqual(mg.name, "It's some kind of magic...")
        self.assertEqual(mg.damage_points, 5)
        self.assertEqual(mg.health_points, 80)

    def test_name_setter_with_empty_string_should_raise_error(self):
        mg  = MagicCard("It's some kind of magic...")
        with self.assertRaises(ValueError) as cm:
            mg.name = ""
        self.assertEqual(str(cm.exception), "Card's name cannot be an empty string.")

    def tests_damage_setter_with_negative_number_should_raise_error(self):
        mg  = MagicCard("It's some kind of magic...")
        with self.assertRaises(ValueError) as cm:
            mg.damage_points = -5
        self.assertEqual(str(cm.exception), "Card's damage points cannot be less than zero.")

    def tests_health_setter_with_negative_number_should_raise_error(self):
        mg  = MagicCard("It's some kind of magic...")
        with self.assertRaises(ValueError) as cm:
            mg.health_points = -5
        self.assertEqual(str(cm.exception), "Card's HP cannot be less than zero.")

    def test_name_setter_with_correct_string_should_change_name(self):
        mg  = MagicCard("It's some kind of magic...")
        mg.name = "Magic Card"
        self.assertEqual(mg.name, "Magic Card")

    def test_damage_setter_with_correct_number_should_change_damage(self):
        mg  = MagicCard("It's some kind of magic...")
        mg.damage_points = 10
        self.assertEqual(mg.damage_points, 10)

    def test_health_setter_with_correct_number_should_change_health(self):
        mg  = MagicCard("It's some kind of magic...")
        mg.health_points = 10
        self.assertEqual(mg.health_points, 10)

if __name__ == "__main__":
    unittest.main()