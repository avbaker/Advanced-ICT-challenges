number = 1976
def getP(number):
    k = number // 3
    n = number % 3

    match n:
        case 0:
            P = 3**k
        case 1:
            P = 2**2 * 3**(k-1)
        case 2:
            P = 2 * 3**k

    return P

num = 2
while num >=2:
    print("Enter a number. you will see the largest number that is the\nproduct of positive integers whose sum is that number.")
    num = int(input(">>> "))
    print(f"{num}: {getP(num)}")
    print("\n type 0 to end.")