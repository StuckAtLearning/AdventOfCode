import pytest
import InputManager as ir


def test_read_file():
    output_int_double_new_line = ir.read_file(
        '../test_inputs/input_manager_test_inputs/double_new_line_int_only.txt', double_new_line=True)
    assert output_int_double_new_line == [[9686, 10178, 3375, 9638], [24919, 15983, 18045], [24872, 35761]]

    output_str_double_new_line = ir.read_file(
        '../test_inputs/input_manager_test_inputs/double_new_line_int_only.txt', parse_int=False, double_new_line=True)
    assert output_str_double_new_line == [['9686', '10178', '3375', '9638'],
                                          ['24919', '15983', '18045'],
                                          ['24872', '35761']]

    output_mixed_int_double_new_line = ir.read_file(
        '../test_inputs/input_manager_test_inputs/double_new_line_mixed_type.txt', double_new_line=True)
    assert output_mixed_int_double_new_line == [[[9686], [10178], [3375], [9638]],
                                                [[24919, 68435], [1598, 76876], [79879, 18045, 54653]],
                                                [[24872, 786859, 767654], [35761, 90432]]]

    output_int_single_new_line = ir.read_file(
        '../test_inputs/input_manager_test_inputs/single_new_line_int_only.txt')
    assert output_int_single_new_line == [9686, 10178, 3375, 9638, 24919, 15983, 18045, 24872, 35761]

    output_str_single_new_line = ir.read_file(
        '../test_inputs/input_manager_test_inputs/single_new_line_int_only.txt', parse_int=False)
    assert output_str_single_new_line == ['9686', '10178', '3375', '9638', '24919', '15983', '18045', '24872', '35761']

    output_mixed_int_single_new_line = ir.read_file(
        '../test_inputs/input_manager_test_inputs/single_new_line_mixed_type.txt')
    assert output_mixed_int_single_new_line == [[9686],
                                                [10178],
                                                [3375],
                                                [9638],
                                                [24919, 68435],
                                                [1598, 76876],
                                                [79879, 18045, 54653],
                                                [24872, 786859, 767654], [35761, 90432]]


def test_parse_int_in_line():
    output = ir.parse_int_in_line(' : 3249 weruhuiqwre723491'' \ 3uh2h4 whiuh83279 32487692.34')
    assert output == [3249, 723491, 3, 2, 4, 83279, 32487692, 34]


def parse_grid():
    assert True
