import time
import sys
sys.setrecursionlimit(1000000)

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response


def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial_r(n-1)

if __name__ == '__main__':
    n = 1000
    it_time_start = time.time()
    factorial_r(n)
    it_time_finish = time.time()
    print(f"Iterative implementation time {it_time_start - it_time_finish}")

    re_time_start = time.time()
    factorial_r(n)
    re_time_finish = time.time()
    print(f"Recursive implementation time {re_time_start - re_time_finish}")
