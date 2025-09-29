import random, math
r = random.randint(100, 9999)/100
print(f"the price is {r:.2f}")

cash = float(input("Please enter the amount tendered"))

if cash > r:
    change = cash - r
    print(f"Thank you. Here is your change: £{change:.2f}")
    poundCoins = change // 1
    change = change - poundCoins
    fiftypence = change // 0.5
    change = change - fiftypence*0.5
    twentypence = change // 0.2
    change = change - twentypence*0.2
    tenpence = change // 0.1
    change = change - tenpence*0.1
    fivepence = change // 0.05
    change = change - fivepence*0.05
    tuppence = change // 0.02
    change = change - tuppence*0.02
    pence = round(change,2) // 0.01
    change = change - pence*0.01
    print(f" pounds:{poundCoins:.0f}. 50p: {fiftypence:.0f} 20p: {twentypence:.0f}, 10p: {tenpence:.0f}, 5p:{fivepence:.0f}, 2p: {tuppence:.0f}, 1p: {pence:.0f}")
else:
    if cash == r:
        print("Exact change! Thanks!")
    else:
        print("You haven't given enough money")
