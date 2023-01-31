import pytest
import InputManager as ir


def test_read_file_with_double_new_line():
    output = ir.read_file_with_double_new_line('../test_inputs/double_new_line_int_only.txt')
    assert output == [['9686', '10178', '3375', '9638'], ['24919', '15983', '18045'], ['24872', '35761']]

