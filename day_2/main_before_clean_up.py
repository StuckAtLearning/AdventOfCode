import ReadFileFunctions as RFF


def follow_strategy_score(strategy_file_path):
    # A = Rock = 1 = X = LOSE
    # B = Paper = 2 = Y = DRAW
    # C = Scissor = 3 = Z = WIN
    # strategy_list = (1 if i == "A" else 2 if i == "B" else 3, 1 if j == "X" else 2 if j == "Y" else 3) for

    strategy_list = RFF.read_file_with_new_line(strategy_file_path)

    strategy_score_list = list()
    for game in strategy_list:
        opponent_choice = game[0]
        self_choice = game[2]

        if opponent_choice == "A":
            opponent_points = 1
        elif opponent_choice == "B":
            opponent_points = 2
        else:
            opponent_points = 3

        if self_choice == "X":
            self_points = 1
        elif self_choice == "Y":
            self_points = 2
        else:
            self_points = 3

        points = (opponent_points, self_points)
        strategy_score_list.append(points)

    your_total_score = 0
    for opponent, you in strategy_score_list:
        if abs(you - opponent) == 1:
            if you > opponent:
                your_total_score += 6
        elif abs(you - opponent) == 0:
            your_total_score += 3
        else:
            if you < opponent:
                your_total_score += 6
        your_total_score += you

    return your_total_score


def the_real_strategy(strategy_file_path):
    # A = Rock = 1 = X = LOSE
    # B = Paper = 2 = Y = DRAW
    # C = Scissor = 3 = Z = WIN
    strategy_list = RFF.read_file_with_new_line(strategy_file_path)

    strategy_score_list = list()
    for game in strategy_list:
        opponent_choice = game[0]
        self_choice = game[2]

        if opponent_choice == "A":
            opponent_points = 1
        elif opponent_choice == "B":
            opponent_points = 2
        else:
            opponent_points = 3

        if self_choice == "X":
            self_points = 0
        elif self_choice == "Y":
            self_points = 3
        else:
            self_points = 6

        points = (opponent_points, self_points)
        strategy_score_list.append(points)

    your_total_score = 0
    for opponent, you in strategy_score_list:
        if you == 6:
            if opponent < 3:
                your_total_score += 1
            else:
                your_total_score -= 2

        elif you == 0:
            if opponent > 1:
                your_total_score -= 1
            else:
                your_total_score += 2

        your_total_score += you + opponent
    return your_total_score


if __name__ == '__main__':
    final_score = follow_strategy_score("encrypted_strategy_guide.txt")
    print(final_score)

    real_game = the_real_strategy("encrypted_strategy_guide.txt")
    print(real_game)
