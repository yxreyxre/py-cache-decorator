from typing import Callable
saved_cache = {}

def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> None:
        if func(args, kwargs) not in saved_cache:
            print("Calculating new result")
            saved_cache[args, kwargs] = func(args, kwargs)
            return func(args, kwargs)
        else:
            print("Getting from cache")
            return saved_cache[args, kwargs]
    return inner

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)



long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func(1, 2, 3)
