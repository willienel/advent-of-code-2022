KEY_ROCK = "Rock"
KEY_PAPER = "Paper"
KEY_SCISSORS = "Scissors"
KEY_WIN = "Win"
KEY_DRAW = "Draw"
KEY_LOSE = "Lose"
KEY_VALUE = "value"

MAPPINGS = {
    "A": KEY_ROCK,
    "B": KEY_PAPER,
    "C": KEY_SCISSORS,
    "X": KEY_ROCK,
    "Y": KEY_PAPER,
    "Z": KEY_SCISSORS
}

OUTCOME_MAPPINGS = {
    "X": KEY_LOSE,
    "Y": KEY_DRAW,
    "Z": KEY_WIN
}

MOVES = {
    KEY_ROCK: {
        KEY_LOSE: KEY_PAPER,
        KEY_DRAW: KEY_ROCK,
        KEY_WIN: KEY_SCISSORS,
        KEY_VALUE: 1
    },
    KEY_PAPER: {
        KEY_LOSE: KEY_SCISSORS,
        KEY_DRAW: KEY_PAPER,
        KEY_WIN: KEY_ROCK,
        KEY_VALUE: 2
    },
    KEY_SCISSORS: {
        KEY_LOSE: KEY_ROCK,
        KEY_DRAW: KEY_SCISSORS,
        KEY_WIN: KEY_PAPER,
        KEY_VALUE: 3
    }
}

POINTS = {
    KEY_LOSE: 0,
    KEY_DRAW: 3,
    KEY_WIN: 6
}


def calculate_scores(entries):

    total_opponent_score = 0
    total_player_score = 0

    for entry in entries:

        opponent_score = 0
        player_score = 0

        opponent, player = entry

        move_opponent = MAPPINGS[opponent]
        move_player = MAPPINGS[player]

        opponent_score += MOVES[move_opponent][KEY_VALUE]
        player_score += MOVES[move_player][KEY_VALUE]

        if MOVES[move_opponent][KEY_DRAW] == move_player:
            opponent_score += POINTS[KEY_DRAW]
            player_score += POINTS[KEY_DRAW]
        elif MOVES[move_opponent][KEY_WIN] == move_player:
            opponent_score += POINTS[KEY_WIN]
            player_score += POINTS[KEY_LOSE]
        else:
            opponent_score += POINTS[KEY_LOSE]
            player_score += POINTS[KEY_WIN]

        total_opponent_score += opponent_score
        total_player_score += player_score

    return total_player_score, total_opponent_score


def calculate_scores_part_two(entries):

    total_opponent_score = 0
    total_player_score = 0

    for entry in entries:

        opponent_score = 0
        player_score = 0

        opponent, player = entry

        match_outcome = OUTCOME_MAPPINGS[player]

        move_opponent = MAPPINGS[opponent]

        if match_outcome == KEY_DRAW:
            move_player = MOVES[move_opponent][KEY_DRAW]
        elif match_outcome == KEY_LOSE:
            move_player = MOVES[move_opponent][KEY_WIN]
        else:
            move_player = MOVES[move_opponent][KEY_LOSE]

        opponent_score += MOVES[move_opponent][KEY_VALUE]
        player_score += MOVES[move_player][KEY_VALUE]

        if match_outcome == KEY_DRAW:
            opponent_score += POINTS[KEY_DRAW]
            player_score += POINTS[KEY_DRAW]
        elif match_outcome == KEY_LOSE:
            opponent_score += POINTS[KEY_WIN]
            player_score += POINTS[KEY_LOSE]
        elif match_outcome == KEY_WIN:
            opponent_score += POINTS[KEY_LOSE]
            player_score += POINTS[KEY_WIN]

        total_opponent_score += opponent_score
        total_player_score += player_score

    return total_player_score, total_opponent_score


def get_test_entries():
    entries = []
    with open("test_input.txt", "r") as f:
        for line in f.readlines():
            opponent, player = line.strip().split(" ")
            entries.append((opponent, player))
    return entries


def get_entries():
    entries = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            opponent, player = line.strip().split(" ")
            entries.append((opponent, player))
    return entries


if __name__ == '__main__':

    # test_entries = get_test_entries()
    #
    # test_player_total_score, _ = calculate_scores(test_entries)
    #
    # print(test_player_total_score)
    #
    # test_player_total_score, _ = calculate_scores_part_two(test_entries)
    #
    # print(test_player_total_score)

    entries = get_entries()

    # Part 1
    player_total_score, _ = calculate_scores(entries)

    print(player_total_score)

    # Part 2
    player_total_score, _ = calculate_scores_part_two(entries)

    print(player_total_score)
