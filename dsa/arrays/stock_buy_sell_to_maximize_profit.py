def naive_stock_buy_sell_to_maximize_profit(stock_nums):
    profit_buy_day, profit_sell_day = 0, 0
    loss_buy_day, loss_sell_day = 0, 0
    max_profit = 0
    min_loss = -float('inf')
    n = len(stock_nums)
    for i in range(n):
        for j in range(i+1, n):
            diff = stock_nums[j] - stock_nums[i]
            
            if diff > 0:  # got profit
                if max_profit < diff:
                    max_profit = diff
                    profit_buy_day, profit_sell_day = i, j
            else:  # got loss
                if min_loss < diff:
                    min_loss = diff
                    loss_buy_day, loss_sell_day = i, j

    if max_profit == 0:
        if min_loss == -float('inf'):
            buy_price, sell_price = None, None
        else:
            buy_price, sell_price = stock_nums[loss_buy_day], stock_nums[loss_sell_day]
    else:
        buy_price, sell_price = stock_nums[profit_buy_day], stock_nums[profit_sell_day]
    
    return buy_price, sell_price


def stock_buy_sell_to_maximize_profit(stock_nums):
    if not stock_nums or len(stock_nums) < 2:
        return None, None

    current_profit = float('-inf')
    current_buy = stock_nums[0]
    global_sell = stock_nums[1]
    global_profit = global_sell - current_buy

    for i in range(1, len(stock_nums)):
        current_profit = stock_nums[i] - current_buy
        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = stock_nums[i]
        if stock_nums[i] < current_buy:
            current_buy = stock_nums[i]
    
    return (global_sell - global_profit), global_sell


if __name__ == '__main__':
    # stock_nums = [7, 1, 5, 3, 6, 4]
    # expected_buy_day, expected_sell_day = 2, 5
    stock_nums = [1, 2, 3, 4, 3, 2, 1, 2, 5]
    expected_buy_day, expected_sell_day = 1, 5
    buy_day, sell_day = naive_stock_buy_sell_to_maximize_profit(stock_nums)

    print(expected_buy_day, expected_sell_day)
    print(buy_day, sell_day)



