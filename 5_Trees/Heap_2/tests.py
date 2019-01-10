from test_helper import run_common_tests, failed, passed, get_answer_placeholders, test_function
from task_2 import *

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":  # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    tests = [
        (26, [20, 8, 22, 4, 12, 10, 14 ], 7, 2, 3),
        (15, [1, 2, 3, 4, 5], 5, 0, 5),
        (-55 ,[-6, -55, 2], 3,1, 2)
    ]
    for test in tests:
        test_function(test[0], sum_between_two_Kth, test[1], test[2], test[3], test[4])
