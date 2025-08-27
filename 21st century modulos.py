def c21Modulos():
    count = 0
    for year in range(2000, 2099):
        syear = str(year)
        for c in syear:
            c = int(c)
            if c % 2 ==1:
                if c % 3 == 1:
                    if c % 5 == 1:
                        if c % 7 == 1:
                            count += 1
                            print(year)
    print(f"the number of years that satisfy the restrictions are {count}.")
c21Modulos()