#unfinished

'''To do this trick manually you need to:

Take 21 cards - they don't need to be playing cards, just 21 different cards.
Ask someone to choose one of the cards from the set of 21.
Deal the cards into three piles, i.e. deal from the top of the pack into piles in the order 1, 2, 3, 1, 2, 3... etc.
Ask the other person which pile their card is in (not which card it is).
Stack the three piles of cards with their selected pile in the middle.
Repeat steps 3, 4 and 5 another two times.
Show the person the 11th card in the pile and say "This is your card!"
Your Task
Your task is to reproduce that process as a computer program with the computer as the magician and the user as the other person. You will need to think about:

the user interface - how will you show the piles of cards, and how will the user pick one?
how you will store the full set of cards
how you will store the three separate piles
how you will put the piles back together
'''

full_set = []
for i in range(21):
    full_set.append(chr(65+i))

choice = input("Choose a number between 0 and 21: ")
chosencard = full_set[int(choice)]
print(f"your card is {chosencard}")
piles = [[],[],[]]
thispile = 0
for i in range(20,0,-1):
    piles[thispile].append(full_set[i])
    thispile = thispile + 1
    if thispile == 3:
        thispile = 0

for pile in piles:
    thisstack = ""
    for card in pile:
        thisstack = thisstack + card + "\n"
    print(thisstack +"\n")
