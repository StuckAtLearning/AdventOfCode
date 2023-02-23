import InputManager as ir


def test_read_file():
    test_file_info = ir.read_file('../test_inputs/input_manager_test_inputs/double_new_line_int_only.txt')
    assert test_file_info == "9686\n10178\n3375\n9638\n\n24919\n15983\n18045\n\n24872\n35761"


def test_group_file_info_with_double_new_line():
    test_file_info = "9686\n10178\n3375\n9638\n\n24919\n15983\n18045\n\n24872\n35761"
    test_grouped_info = ir.group_file_info_with_double_new_line(test_file_info)
    assert test_grouped_info == [['9686', '10178', '3375', '9638'], ['24919', '15983', '18045'], ['24872', '35761']]


def test_group_file_info_with_single_new_line():
    test_file_info = "9686\n10178\n3375\n9638\n24919\n15983\n18045\n24872\n35761"
    test_grouped_info = ir.group_file_info_with_single_new_line(test_file_info)
    assert test_grouped_info == ['9686', '10178', '3375', '9638', '24919', '15983', '18045', '24872', '35761']


def test_parse_int_in_line():
    output_positive = ir.parse_int_in_line(' : 3249 weruhuiqwre723491'' \ 3uh2h4 whiuh83279 32487692.34')
    assert output_positive == (3249, 723491, 3, 2, 4, 83279, 32487692, 34)

    output_negative = ir.parse_int_in_line(' : -3249 weruhuiqwre-723491'' \ 3uh-2h4 whiuh83279 32487692.34', True)
    assert output_negative == (-3249, -723491, 3, -2, 4, 83279, 32487692, 34)


def test_parse_grid():
    assert True


def test_parse_directions():
    output_directions = ir.parse_directions(">>^v<<^<<>vv>")
    assert output_directions == [(1, 0), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, 0), (0, 1), (-1, 0), (-1, 0), (1, 0),
                                 (0, -1), (0, -1), (1, 0)]

