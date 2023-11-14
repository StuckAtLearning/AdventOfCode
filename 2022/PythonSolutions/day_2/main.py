import ReadFileFunctions as RFF


def follow_strategy_score(strategy_file_path: str) -> int:
    # A = Rock = 1 = X = LOSE
    # B = Paper = 2 = Y = DRAW
    # C = Scissor = 3 = Z = WIN
    strategy_list = RFF.read_file_with_new_line(strategy_file_path)

    # Is it really a clean-up if I'm making it worse?
    # separated_strategy_list = map(lambda x: (x.split(" ")[0], x.split(" ")[1]), strategy_list)
    # strategy_point_list = sum(map(lambda y:
    #                         map(lambda x:
    #                             1 if ((x == "A") or (x == "X")) else 2 if ((x == "B") or (x == "Y")) else 3, y),
    #                                 separated_strategy_list))
    # No, no this is not a clean-up at this point, this is a fuck-up
    # Let's do something normal
    strategy_score_list = [[1 if ((i == "A") or (i == "X")) else 2 if ((i == "B") or (i == "Y")) else 3
                      for i in each_game.split(" ")] for each_game in strategy_list]
    your_total_score = sum(map(lambda x: x[1], strategy_score_list))

    for opponent, you in strategy_score_list:
        if abs(you - opponent) == 1:
            if you > opponent:
                your_total_score += 6
        elif you == opponent:
            your_total_score += 3
        else:
            if you < opponent:
                your_total_score += 6

    return your_total_score


def the_real_strategy(strategy_file_path: str) -> int:
    # A = Rock = 1 = X = LOSE
    # B = Paper = 2 = Y = DRAW
    # C = Scissor = 3 = Z = WIN
    strategy_list = RFF.read_file_with_new_line(strategy_file_path)

    # same thing here because I am too lazy to list comprehend these
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

    your_total_score = sum([i + j for i, j in strategy_score_list])
    for opponent, you in strategy_score_list:
        if you == 6:
            # opponent chooses Rock or Paper
            if opponent < 3:
                # you need choose Paper or Scissor, which would be one point more than your opponent's choice points
                your_total_score += 1
            # opponent chooses Scissors
            else:
                # you need to choose Rock which is two points less than your opponent's choice points
                your_total_score -= 2

        # you need to lose
        elif you == 0:
            # opponent chooses Paper or Scissors
            if opponent > 1:
                # you need to choose Rock or Paper
                your_total_score -= 1
            # opponent chooses Rock
            else:
                # you need to choose Scissors
                your_total_score += 2

    return your_total_score


if __name__ == '__main__':
    final_score = follow_strategy_score("real_input.txt")
    print(final_score)

    real_game = the_real_strategy("real_input.txt")
    print(real_game)