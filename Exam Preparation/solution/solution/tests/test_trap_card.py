from project.card.trap_card import TrapCard
import unittest

class TestsTrapCard(unittest.TestCase):
    def test_init_should_create_all_attributes(self):
        tc  = TrapCard("It's some kind of magic...")
        self.assertEqual(tc.name, "It's some kind of magic...")
        self.assertEqual(tc.damage_points, 120)
        self.assertEqual(tc.health_points, 5)

  
if __name__ == "__main__":
    unittest.main()