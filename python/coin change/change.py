def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
        
    min_coins = [target + 1] * (target + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    if min_coins[target] == target + 1:
        raise ValueError("can't make target with given coins")
        
    answer = []
    while target:
        for coin in coins:
            remainder = target - coin
            if remainder < 0:
                continue
            if min_coins[target] == min_coins[remainder] + 1:
                answer.append(coin)
                break
        target -= coin

    return answer
