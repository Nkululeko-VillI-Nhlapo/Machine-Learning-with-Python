# DO NOT MODIFY THIS FILE

import random

# Function to simulate a series of Rock-Paper-Scissors games between two players
def play(player1, player2, num_games, verbose=False):
    """
    Simulates a series of Rock-Paper-Scissors games between two players.

    Args:
    - player1 (function): Function representing player 1's strategy.
    - player2 (function): Function representing player 2's strategy.
    - num_games (int): Number of games to simulate.
    - verbose (bool, optional): If True, print game details; default is False.

    Returns:
    - float: Win rate of player 1 as a percentage.

    """
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        # Get current plays from players based on each other's previous plays
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        # Determine the winner of each game
        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif (p2_play == "P" and p1_play == "R") or (
                p2_play == "R" and p1_play == "S") or (p2_play == "S"
                                                       and p1_play == "P"):
            results["p2"] += 1
            winner = "Player 2 wins."

        # Print game details if verbose mode is enabled
        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        # Update previous plays for next iteration
        p1_prev_play = p1_play
        p2_prev_play = p2_play

    # Calculate win rate for player 1
    games_won = results['p2'] + results['p1']
    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    # Print final results and return win rate
    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return win_rate


# Example player strategies for Rock-Paper-Scissors
def quincy(prev_play, counter=[0]):
    """
    Simple strategy player named Quincy.

    Args:
    - prev_play (str): Opponent's last play.
    - counter (list, optional): Counter for tracking plays; default is [0].

    Returns:
    - str: Next play based on counter.

    """
    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def mrugesh(prev_opponent_play, opponent_history=[]):
    """
    Strategy player named Mrugesh based on opponent history.

    Args:
    - prev_opponent_play (str): Opponent's last play.
    - opponent_history (list, optional): List of opponent's previous plays; default is [].

    Returns:
    - str: Next play based on opponent's most frequent play.

    """
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]


def kris(prev_opponent_play):
    """
    Strategy player named Kris.

    Args:
    - prev_opponent_play (str): Opponent's last play.

    Returns:
    - str: Next play based on opponent's last play.

    """
    if prev_opponent_play == '':
        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prev_opponent_play]


def abbey(prev_opponent_play,
          opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    """
    Strategy player named Abbey based on opponent history and play order.

    Args:
    - prev_opponent_play (str): Opponent's last play.
    - opponent_history (list, optional): List of opponent's previous plays; default is [].
    - play_order (list, optional): List tracking play order; default is [{}].

    Returns:
    - str: Next play based on opponent's play order prediction.

    """
    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]


def human(prev_opponent_play):
    """
    Strategy player representing a human input.

    Args:
    - prev_opponent_play (str): Opponent's last play.

    Returns:
    - str: Next play based on user input.

    """
    play = ""
    while play not in ['R', 'P', 'S']:
        play = input("[R]ock, [P]aper, [S]cissors? ")
        print(play)
    return play


def random_player(prev_opponent_play):
    """
    Strategy player representing a random choice.

    Args:
    - prev_opponent_play (str): Opponent's last play.

    Returns:
    - str: Randomly chosen play ('R', 'P', or 'S').

    """
    return random.choice(['R', 'P', 'S'])
