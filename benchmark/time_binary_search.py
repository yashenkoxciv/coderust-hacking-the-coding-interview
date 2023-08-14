import timeit
import random
from loguru import logger
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, './')  # to import dsa
from dsa.binary_search import binary_search, binary_search_recursive


NUMBER = 10
REPEAT = 5


def best(t, digits=4):
    return round(min(t), digits)


def get_random_int_list(n):
    a = [random.randint(0, 100_000) for _ in range(n)]
    return a


random_nums_100 = get_random_int_list(100)
random_nums_1000 = get_random_int_list(1000)
random_nums_10k = get_random_int_list(10_000)
random_nums_50k = get_random_int_list(50_000)
random_nums_100k = get_random_int_list(100_000)
random_nums_500k = get_random_int_list(500_000)
random_nums_1m = get_random_int_list(1_000_000)


def binary_search_100():
    nums = sorted(random_nums_100)
    target = random_nums_100[0]  # random number
    binary_search(nums, target)


def binary_search_1000():
    nums = sorted(random_nums_1000)
    target = random_nums_1000[0]  # random number
    binary_search(nums, target)


def binary_search_10k():
    nums = sorted(random_nums_10k)
    target = random_nums_10k[0]  # random number
    binary_search(nums, target)


def binary_search_50k():
    nums = sorted(random_nums_50k)
    target = random_nums_50k[0]  # random number
    binary_search(nums, target)


def binary_search_100k():
    nums = sorted(random_nums_100k)
    target = random_nums_100k[0]  # random number
    binary_search(nums, target)


def binary_search_500k():
    nums = sorted(random_nums_500k)
    target = random_nums_500k[0]  # random number
    binary_search(nums, target)


def binary_search_1m():
    nums = sorted(random_nums_1m)
    target = random_nums_1m[0]  # random number
    binary_search(nums, target)


def main():
    ests = []
    isize = [100, 1000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
    logger.info('run 100 benchmark')
    t = timeit.repeat(binary_search_100, number=NUMBER, repeat=REPEAT)
    t_call_estimate = sum(t) / (NUMBER*REPEAT)
    ests.append(t_call_estimate)
    logger.success(f'{t_call_estimate:3.10f}')

    logger.info('run 1000 benchmark')
    t = timeit.repeat(binary_search_1000, number=NUMBER, repeat=REPEAT)
    t_call_estimate = sum(t) / (NUMBER*REPEAT)
    ests.append(t_call_estimate)
    logger.success(f'{t_call_estimate:3.10f}')

    logger.info('run 10k benchmark')
    t = timeit.repeat(binary_search_10k, number=NUMBER, repeat=REPEAT)
    t_call_estimate = sum(t) / (NUMBER*REPEAT)
    ests.append(t_call_estimate)
    logger.success(f'{t_call_estimate:3.10f}')

    logger.info('run 50k benchmark')
    t = timeit.repeat(binary_search_50k, number=NUMBER, repeat=REPEAT)
    t_call_estimate = sum(t) / (NUMBER*REPEAT)
    ests.append(t_call_estimate)
    logger.success(f'{t_call_estimate:3.10f}')

    logger.info('run 100k benchmark')
    t = timeit.repeat(binary_search_100k, number=NUMBER, repeat=REPEAT)
    t_call_estimate = sum(t) / (NUMBER*REPEAT)
    ests.append(t_call_estimate)
    logger.success(f'{t_call_estimate:3.10f}')

    logger.info('run 500k benchmark')
    t = timeit.repeat(binary_search_500k, number=NUMBER, repeat=REPEAT)
    t_call_estimate = sum(t) / (NUMBER*REPEAT)
    ests.append(t_call_estimate)
    logger.success(f'{t_call_estimate:3.10f}')

    logger.info('run 1m benchmark')
    t = timeit.repeat(binary_search_1m, number=NUMBER, repeat=REPEAT)
    t_call_estimate = sum(t) / (NUMBER*REPEAT)
    ests.append(t_call_estimate)
    logger.success(f'{t_call_estimate:3.10f}')

    plt.plot(isize, ests)
    plt.savefig('fig.jpg')


if __name__ == '__main__':
    main()

