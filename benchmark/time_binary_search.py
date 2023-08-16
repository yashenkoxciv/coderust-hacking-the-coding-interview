import timeit
import random
import functools
from loguru import logger
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, './')  # to import dsa
from dsa.binary_search import binary_search, binary_search_recursive


class BinarySearchDataSource:
    def get_unsorted_data(self, n):
        nums = BinarySearchDataSource.get_random_int_list(n)
        target = nums[0]
        return nums, target

    def get_sorted_data(self, n):
        nums, target = self.get_unsorted_data(n)
        sorted_nums = sorted(nums)
        return sorted_nums, target
    
    @staticmethod
    def get_random_int_list(n):
        a = [random.randint(0, 100_000) for _ in range(n)]
        return a


def binary_search_unsorted(nums, target):
    sorted_nums = sorted(nums)
    return binary_search(sorted_nums, target)


def time_estimate(job, number, repeat):
    t = timeit.repeat(job, number=number, repeat=repeat)
    time_for_run = sum(t) / (number*repeat)
    return time_for_run


def run_benchmark(ns: list, number=1_000_000, repeat=5):
    logger.info('Start benchmark')
    bsds = BinarySearchDataSource()

    bs_t_est = []
    unsort_bs_t_est = []
    for n in ns:
        logger.info(f'binary_search (sorted) {n} benchmark')

        nums, target = bsds.get_sorted_data(n)
        binary_search_job = functools.partial(binary_search, nums, target)

        time_for_run = time_estimate(binary_search_job, number, repeat)
        bs_t_est.append(time_for_run)

        logger.info(f'binary_search (unsorted) {n} benchmark')

        nums, target = bsds.get_unsorted_data(n)
        binary_search_unsorted_job = functools.partial(binary_search_unsorted, nums, target)

        time_for_run = time_estimate(binary_search_unsorted_job, number, repeat)
        unsort_bs_t_est.append(time_for_run)
    return bs_t_est, unsort_bs_t_est



if __name__ == '__main__':
    #[100, 1000, 10_000, 100_000, 500_000, 1_000_000]
    ns = [100, 1000, 2000, 3000]
    bs_t_est, unsort_bs_t_est = run_benchmark(ns)

    plt.plot(ns, bs_t_est)
    plt.plot(ns, unsort_bs_t_est)
    plt.savefig('example.jpg')



    


