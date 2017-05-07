#!/usr/bin/env python3

from contextlib import contextmanager
import time

from main import has_subset_sum_zero


@contextmanager
def less_than(secs):
    tic = time.time()
    yield
    elapsed = time.time() - tic
    print(f'Duration: {elapsed} seconds')
    if elapsed >= secs:
        print('Limit reached. Stopping.')
        raise SystemExit(0)


def do():
    for n in range(1, 100, 10):
        source = range(1, n)
        print(f'Length: {n} items')
        with less_than(300):
            result = has_subset_sum_zero(source)
            print(f'Result: {result}')
        print('Continue...')
        print()


if __name__ == '__main__':
    do()
