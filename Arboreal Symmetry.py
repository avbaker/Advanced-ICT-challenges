def makeTree(base):
    for i in range(0,base,2):
        gaps = (base - i) //2
        print(" "*gaps + "*"*i + " "*gaps)
    print(" "*((base - 1)//2) + "||")
    print(" " * ((base - 1) // 2) + "||")


makeTree(30)