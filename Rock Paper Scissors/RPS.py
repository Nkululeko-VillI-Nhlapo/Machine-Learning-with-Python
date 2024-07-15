def player(prev_play, opponent_history=[], sequences={}):
    """
    A strategy player function for Rock-Paper-Scissors that tracks opponent history
    and predicts the next move based on sequences of plays.

    Args:
    - prev_play (str): Opponent's last play.
    - opponent_history (list, optional): List of opponent's previous plays; default is [].
    - sequences (dict, optional): Dictionary tracking sequences of plays; default is {}.

    Returns:
    - str: Next play predicted based on opponent's history and sequences.

    """
    stride = 3  # Number of plays to consider in each sequence

    # Keep track of the opponent history
    if prev_play != '':
        opponent_history.append(prev_play)

    # If there's not enough data to predict, default to "R" (Rock)
    if len(opponent_history) <= stride:
        return "R"

    # Cap opponent_history to the last `stride + 1` plays
    if len(opponent_history) > stride + 1:
        opponent_history.pop(0)

    # Increment the count of the current sequence
    seq = "".join(opponent_history)
    sequences[seq] = sequences.get(seq, 0) + 1

    # Predict the next move based on the most frequent sequence ending in "R", "P", or "S"
    seq = "".join(opponent_history[-stride:])
    predict = max([seq + "R", seq + "P", seq + "S"],
                  key=lambda key: sequences.get(key, 0))[-1]

    # Return the predicted move based on the predicted sequence
    if predict == "R":
        return "P"  # If predicted to play "R", counter with "P" (Paper)
    elif predict == "P":
        return "S"  # If predicted to play "P", counter with "S" (Scissors)
    else:
        return "R"  # If predicted to play "S", counter with "R" (Rock)
