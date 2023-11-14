import ReadFileFunctions as RFF
import numpy as np


def part_1(input_file_path: str) -> tuple[int, int]:
    test_input = RFF.read_file_with_new_line(input_file_path)
    test_input = np.array([list(line) for line in test_input])

    trees = test_input.astype(int)
    visible_tree_rows = find_trees(trees[1:-1])
    # print(visible_tree_rows[:, 1:-1])
    visible_tree_columns = find_trees(np.transpose(trees)[1:-1])

    all_visible_trees = visible_tree_rows[:, 1:-1] | np.transpose(visible_tree_columns[:, 1:-1])
    # print(all_visible_trees)
    visible_inner_tress = all_visible_trees.sum()
    border_trees = trees.shape[0] * 2 + trees.shape[1] * 2 - 4
    sum_visible_trees = visible_inner_tress + border_trees

    tree_scores_row = get_scores(trees[1:-1])
    tree_scores_column = get_scores(np.transpose(trees)[1:-1])
    # print(tree_scores_row)
    all_tree_scores = np.multiply(tree_scores_row[:, 1:-1], np.transpose(tree_scores_column[:, 1:-1]))
    max_score = np.amax(all_tree_scores)

    return sum_visible_trees, max_score


def find_trees(tree_array):
    visible_trees = np.zeros(tree_array.shape, dtype=bool)
    for j in range(tree_array.shape[0]):
        for k in range(1, tree_array.shape[1] - 1):
            check_row = tree_array[j] < tree_array[j][k]
            if (np.all(check_row[:k])) or (np.all(check_row[k + 1:])):
                visible_trees[j][k] = True
    return visible_trees

    # highest_trees = np.amax(tree_array, axis=1)
    # for i in range(len(highest_trees)):
    #     visible_row = tree_array[i] == highest_trees[i]
    #     visible_trees[i] = visible_row | visible_trees[i]


def get_scores(tree_array):
    tree_scores = np.zeros(tree_array.shape, dtype=int)
    for j in range(tree_array.shape[0]):
        for k in range(1, tree_array.shape[1] - 1):
            check_row = tree_array[j] < tree_array[j][k]
            # get the index of the first false counting from element's left, count all trues
            # get the index of the first false counting from element's right, count all trues
            left_false = np.where(check_row[:k] == False)[0]
            right_false = np.where(check_row[k + 1:] == False)[0]
            left_score = k if not left_false.size > 0 else k - left_false[-1]
            right_score = tree_array.shape[1] - k - 1 if not right_false.size > 0 else right_false[0] + 1
            # print('x =', k, 'y =', j, 'tree =', tree_array[j][k], left_false, right_false, left_score, right_score)
            tree_scores[j][k] = left_score * right_score

    # print(tree_scores)
    return tree_scores


if __name__ == '__main__':
    test_visible_tree, test_tree_score = part_1("test_input.txt")
    print(test_visible_tree, test_tree_score)

    real_visible_tree, real_tree_score = part_1("real_input.txt")
    print(real_visible_tree, real_tree_score)
