import io
import sys
from day_1 import python_solution as ps1
from day_2 import python_solution as ps2


def test_day_1():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    ps1.get_answers()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "138\n1771\n"


def test_day_2():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    ps2.get_answers()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "1586300\n3737498\n"


