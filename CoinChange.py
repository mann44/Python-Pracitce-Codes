#Goolgecoding Youtube Practice
#Greedy Algo
def min_coins(cents):
    if cents < 1:
        return 0
    coins = [25, 10, 5, 1]
    num_of_coins = 0
    for coin in coins:
        #print("Coin count:",num_of_coins)
        if cents / coin >= 1:
            num_of_coins = num_of_coins +  int(cents / coin)
        #print("Nuber of Coins:",num_of_coins)
        cents = cents % coin
        #print("Cents:",cents)
        if cents == 0:
            break
    return num_of_coins

print (int(min_coins(182)))