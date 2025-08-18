doors = []
for i in range(1, 101):
    doors.append(False)  # All doors are initially closed (False)

for i in range(1, 101):
    for j in range(i - 1, 100, i):
        doors[j] = not doors[j]  # Toggle the state of the door

for i in range(1, 100):
    print(f"door: {i}: {'O' if not doors[i] else 'X'}") #print status of all doors

'''
The data shows the gaps between closed doors increases as you go along.

First there are 2 open doors, then 4, then six, etc...
'''

        