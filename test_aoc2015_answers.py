from day_1 import python_solution as ps1
from day_2 import python_solution as ps2
from day_3 import python_solution as ps3
from day_4 import python_solution as ps4


def test_answers():
    day_1_answers = ps1.get_answers()
    assert day_1_answers == (138, 1771)

    day_2_answers = ps2.get_answers()
    assert day_2_answers == (1586300, 3737498)

    day_3_answers = ps3.get_answers()
    assert day_3_answers == (2081, 2341)

    day_4_answers = ps4.get_answers()
    assert day_4_answers == (346386, 9958218)



