import random

'''
Taking a number between 1 and 10000
using randrange function
'''
start = 1
end = 10000
num = random.randrange(start, end+1)

#Now choosing the first digit of num from left...

num_2 = str(num)[0]
num_2 = int(num_2)

'''
Finally, choosing the number for the die
'''
if num_2 < 6:
    roll = random.randrange(1, num_2+1)
elif num_2 == 6:
    roll = num_2

else:
    num_2 = num_2 - 3
    roll = random.randrange(1, num_2+1)

print("You got", roll)
input("Press Enter to exit.")
