from time import time
from functions import lazy_function


def test_test_lazy_function_performance():
    start = time()
    lazy_function()
    end = time()
    duration = end - start
    assert duration < 2.1, "it took more than expected to execute"
