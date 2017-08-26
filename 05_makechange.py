amount (4c)
demoninations (1,2,3)

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢

1c -> x4
2c -> x2
3c -> x1
    recurse on amount - 4

1
    1   1
            1
        2
    2   1
2
    1

BUT - 1, 1, 2 and 2, 1, 1 are the same

take out one coin of each if possible
recurse on solution

so instead of for c in demoninations, we do
        for c in demoninations
            for numTimes in possibleNumberOfTimes(c)

def makechange(amount, demoninations):
    ways = 0
    for c in demoninations:
        if c < amount:
            makechange(amount-c, demoninations)
        if c = amount:
            ways += 1
            # moreways = makechange(amount-c, demoninations)
            # if moreways > 0:
            #     ways += moreways
    return ways

