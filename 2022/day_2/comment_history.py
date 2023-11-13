import ReadFileFunctions as RFF


def follow_strategy_score(strategy_file_path):
    # A = Rock = 1 = X
    # B = Paper = 2 = Y
    # C = Scissor = 3 = Z
    strategy_list = RFF.read_file_with_new_line(strategy_file_path)

    strategy_score_list = list()
    # assign each letter to its corresponding points
    # stored in a list of tuples
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
        # calculate the score by always adding your choice points
        your_total_score += you
        # then determine and add the outcome point:
        # Rock-Paper or Paper-Scissor combo
        if abs(you - opponent) == 1:
            if you > opponent:
                your_total_score += 6
        # Draw
        elif you == opponent:
            your_total_score += 3
        # Rock-Scissor combo
        else:
            if you < opponent:
                your_total_score += 6
        # You always win your choice points

    return your_total_score


def the_real_strategy(strategy_file_path):
    # A = Rock = 1 = X = LOSE
    # B = Paper = 2 = Y = DRAW
    # C = Scissor = 3 = Z = WIN
    strategy_list = RFF.read_file_with_new_line(strategy_file_path)

    strategy_score_list = list()
    # similar as above
    # except XYZ will be assigned to the outcome points instead of choice points
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
        # a little different from Part 1
        # calculate the points by always adding your outcome points and opponent's point
        your_total_score += you + opponent
        # then determine what choice you need to make to WIN/DRAW/LOSE
        # and then add the difference between that choice points and your opponent's choice points
        # you need to win
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

    # 1st Part Answer: 9241
    # 2nd Part Answer: 14610