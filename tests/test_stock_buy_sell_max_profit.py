import pytest
from dsa.arrays.stock_buy_sell_to_maximize_profit import (
    naive_stock_buy_sell_to_maximize_profit
)


examples = [
    # ([7, 1, 5, 3, 6, 4],        2,      5),
    # ([21, 12, 11, 9, 6, 3],     2,      3),
    # ([1, 2, 3, 4, 3, 2, 1, 2, 5],       1,      5),
    ([1, 2, 3, 4, 3, 2, 1, 2, 5],       1,      5),
    ([8, 6, 5, 4, 3, 2, 1],             6,      5),
    ([12, 30, 40, 90, 110],             12,     110),
    ([2],                               None,   None),
    ([1, 2],                            1,      2)
]

test_cases = [
    *examples
]


@pytest.mark.parametrize('stock_nums,expected_buy_day,expected_sell_day', test_cases)
def test_naive_stock_buy_sell_to_maximize_profit(stock_nums, expected_buy_day, expected_sell_day):
    buy_day, sell_day = naive_stock_buy_sell_to_maximize_profit(stock_nums)

    assert buy_day == expected_buy_day
    assert sell_day == expected_sell_day

