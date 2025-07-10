from typing import Callable
saved_cache = []

def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> str:
        if func(*args, **kwargs) not in saved_cache:
            print("Calculating new result")
            saved_cache.append(func(*args, **kwargs))
            return func(*args, **kwargs)
        else:
            print("Getting from cache")
            return saved_cache[func(*args, **kwargs)]
    return inner
