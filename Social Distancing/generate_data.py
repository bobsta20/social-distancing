import sys
import random

size_x = int(sys.argv[1])
size_y = int(sys.argv[2])
amount = int(sys.argv[3])

history = {}

print(str(size_x) + " " + str(size_y))
for i in range(amount):
    x=-1
    y=-1
    while True:
        x = random.randint(0,size_x-1)
        y = random.randint(0, size_y-1)
        try:
            result = history[(x,y)]
        except:
            break
    history[(x,y)] = True
    print(str(x) + " " + str(y))

