import random
import time
from typing import Callable, TypeVar, ParamSpec
from functools import wraps


P = ParamSpec("P")
R = TypeVar("R")


def timelog(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def logger(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"--- {func.__name__} starts ---")
        start_t = time.time()
        value = func(*args, **kwargs)
        end_t = time.time()
        print(f"--- {func.__name__} ended, and used {end_t - start_t:.2f} s---")
        return value
    return logger


@timelog
def example_func2():
   random_delay = random.randint(3, 5) * 0.1
   time.sleep(random_delay)


example_func2()

