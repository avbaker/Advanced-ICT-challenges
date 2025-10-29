import random
min = 5
max = 5
n1 = random.randint(min, max)
n2 = random.randint(min, max)
n3 = random.randint(min, max)

print(f"n1 + n2 = {n1 + n2}\nn2 + n3 = {n2 + n3}\nn1 + n3 = {n1 + n3}\n\nWhat is the value of n1, n2 and n3?\n\nAnswer in the format 'n1,n2,n3'.")

ans = input()
ans = ans.split(',')
if int(ans[0]) == n1 and int(ans[1]) == n2 and int(ans[2]) == n3:
    print("Correct!")
else:
    print("Incorrect!")