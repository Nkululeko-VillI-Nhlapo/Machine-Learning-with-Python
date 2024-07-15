import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player

# Define a unit test class for Rock-Paper-Scissors game players
class UnitTests(unittest.TestCase):
    print()  # This print statement seems unnecessary; it doesn't affect the code's functionality.

    # Test case to evaluate player performance against quincy
    def test_player_vs_quincy(self):
        print("Testing game against quincy...")
        actual = play(player, quincy, 1000) >= 60  # Play 1000 games and check if player wins at least 60% of the time
        self.assertTrue(
            actual,
            'Expected player to defeat quincy at least 60% of the time.'
        )

    # Test case to evaluate player performance against abbey
    def test_player_vs_abbey(self):
        print("Testing game against abbey...")
        actual = play(player, abbey, 1000) >= 60  # Play 1000 games and check if player wins at least 60% of the time
        self.assertTrue(
            actual,
            'Expected player to defeat abbey at least 60% of the time.'
        )

    # Test case to evaluate player performance against kris
    def test_player_vs_kris(self):
        print("Testing game against kris...")
        actual = play(player, kris, 1000) >= 60  # Play 1000 games and check if player wins at least 60% of the time
        self.assertTrue(
            actual,
            'Expected player to defeat kris at least 60% of the time.'
        )

    # Test case to evaluate player performance against mrugesh
    def test_player_vs_mrugesh(self):
        print("Testing game against mrugesh...")
        actual = play(player, mrugesh, 1000) >= 60  # Play 1000 games and check if player wins at least 60% of the time
        self.assertTrue(
            actual,
            'Expected player to defeat mrugesh at least 60% of the time.'
        )

# Run the unit tests if this script is executed directly
if __name__ == "__main__":
    unittest.main()
