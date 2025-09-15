'''There are many different ways to calculate π, including using random numbers and something called the Monte Carlo method.
A more common method is to use a mathematical sequence such as the Leibniz formula. This can be summarised as follows:

"Take 4, subtract 4/3, add 4/5, subtract 4/7, and so on."

Task
Your task is to write a program that uses this method to calculate the value of π. It should:

use repetition so that you can choose the number of terms in the sequence (you can't say "and so on" in your program!)
include a way to alternate between addition and subtraction
show how the sequence converges (i.e. homes in on the answer) as it progresses
This sequence converges quite slowly - can you see how many terms you need to calculate to find π to five decimal places?
'''


def calcPi(loops):
    add = False
    num = 3
    ans = 4.0
    for i in range(1, loops+1):
        if add:
            ans = ans + (4/num)
        else:
            ans = ans - (4/num)
        num += 2
        add = not add
        print(ans, num)


loops = int(input("How many iterations of the algorithm do you want to calculate? "))
calcPi(loops)