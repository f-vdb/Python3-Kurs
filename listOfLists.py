import copy
import itertools
lines = [ [ [1, 1, 1], 7], [ [2, 2, 2], 5] ]

tmp = copy.deepcopy(lines)
x = tmp.pop()


x[0][2] += 1

print(x)
print(lines)

degree = 6
x[1] = degree
print(x)

lines.extend(x)
print(lines)


permutations = itertools.permutations([1,2,3,4,5,6,7,8,9,10], 3)
listOfPermutations = list(permutations)
print(listOfPermutations)
print(listOfPermutations[0])
print(listOfPermutations[0][1])

class Value():
    def __init__(self, a, b, c, z):
        self.a = a
        self.b = b
        self.c = c
        self.z = z

    def printValues(self):
        print("a =", self.a, " b =", self.b, " c =", self.c, "c =", self.z)

    def getABC(self):
        return self.a, self.b, self.c

    def searchAndReplace(self, searchA, searchB, searchC, replaceZ):
        if self.a == searchA and self.b == searchB and self.c == searchC:
            self.z = replaceZ



values = []
for items in listOfPermutations:
    a,b,c = items
    tmp = Value(a,b,c, -1)
    values.append(tmp)

for value in values:
    value.printValues()

for value in values:
    value.searchAndReplace(10, 9, 8, 99)

for value in values:
    value.printValues()



'''
# Dictionaries -> unhashable type 'list'
new = {[1,1,1]: 7,
       [2,2,2]: 5}

x = new[[2,2,2]]
print(new)

'''
