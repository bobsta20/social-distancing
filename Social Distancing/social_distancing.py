import sys
from queue import PriorityQueue

#checks if a place has been visited before
def is_visited(x,y, path):
    for i in range(len(path)):
        if path[i] == (x,y):
            return True
    return False

#Determines valid neighbours of a point
def get_possibilities(x,y,path):
    possibilities = []
    if x >0:
        if not is_visited(x-1,y, path):
            possibilities.append((x-1,y))
    if x < len(space)-1:
        if not is_visited(x+1,y,path):
            possibilities.append((x+1,y))
    if y > 0:
        if not is_visited(x,y-1, path):
            possibilities.append((x,y-1))
    if y < len(space[0])-1:
        if not is_visited(x,y+1, path):
            possibilities.append((x,y+1))
    return possibilities

#gets the minimum distance from a list of distances
def get_minimum(distances):
    minimum = distances[0]
    for i in range(len(distances)-1):
        if distances[i+1] < minimum:
            minimum = distances[i+1]
    return minimum

#gets the distances
def get_distances(x,y):
    distances = []
    for i in range(len(people)):
        distances.append(abs(x - people[i][0]) + abs(y - people[i][1]))
    return distances

#Solves a scenario
def solve():
    #Calculates maximum distances from each person
    maximum_distances = []
    for i in range(len(people)):
        #If they go over the top they have to go to its right to get to the end
        top = people[i][0]
        right = len(space[0]) - people[i][1] - 1
        if top < right:
            maximum= top
        else:
            maximum = right
        #If they go past the left they have to go below to get to the end
        bottom = len(space) - people[i][0] - 1
        left = people[i][1]
        if left < bottom:
            if left > maximum:
                maximum = left
        else:
            if bottom > maximum:
                maximum = bottom
        maximum_distances.append(maximum)

    queue = PriorityQueue()
    #Priority is in order of minimum distance
    queue.put(((get_minimum(maximum_distances)*-1, (len(space)+len(space[0])-2)), (0,0, [])))
    count = 0
    history = {}
    #Doing the search:
    while True:
        count+=1
        current = queue.get()
        x = current[1][0]
        y = current[1][1]
        current_minimum = current[0][0] * -1
        path = current[1][2].copy()
        path.append((x,y))
        possibilities = get_possibilities(x,y,path)
        for i in range(len(possibilities)):
            x = possibilities[i][0]
            y = possibilities[i][1]
            try:
                result = history[(x,y)]
                continue
            except:
                history[(x,y)] = True
            minimum = get_minimum(get_distances(x,y))
            if minimum > current_minimum:
                minimum = current_minimum
            distance = len(space) - 1-x + len(space[0]) - 1-y
            if distance == 0:
                print("min " + str(minimum))
                print(count)
                return
            queue.put(((minimum*-1, distance), (x,y,path)))

#Reads in input and processes it
firstLine = True
space = []
people = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        solve()
        firstLine = True
        space = []
        people = []
        continue
    line = line.split(" ")
    if firstLine:
        for i in range(int(line[0])):
            space.append([])
            for j in range(int(line[1])):
                space[i].append(0)
        firstLine = False
        continue
    people.append((int(line[0]), int(line[1])))
    space[int(line[0])][int(line[1])] = 1
#Solves last Scenario
if space != []:
    solve()