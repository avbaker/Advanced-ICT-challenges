def calculate_chocolate_bars(money, price, freeEvery):
    totalBars = 0
    totalBars += money/price #total bars bought
    totalBars += totalBars / freeEvery #free bars
    return int(totalBars)

def calculate_chocolate_bars_loop(money, price, freeEvery):
    totalBars = 0
    while money > price: #while you can still buy more
        if totalBars % freeEvery == 0: #check for free bar and award
            totalBars += 1
        totalBars += 1 #buy a bar
        money = money-price
    if totalBars % freeEvery == 0:  # check for free bar and award
        totalBars += 1
    return totalBars

print(f"At most, you can get {calculate_chocolate_bars_loop(1000,1, 4)} bars.")
