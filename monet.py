coins = [0.01, 0.05, 0.1, 0.5, 1, 2, 5, 10, 25]


def exchange(mony):
    count, summ = 0, 0
    for coin in coins:
        summ = mony // coin
        if summ == 0:
            count += 1
        else:
            exchange(summ)


exchange(10)