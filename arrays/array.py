class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def arrinsert(self, n):
        self.data[self.size] = n
        self.size += 1

    def insertatend(self, n):
        self.capacity += 1
        self.data += [None] * 1
        self.data[self.size] = n
        self.size += 1

    def insertatbeginning(self, n):
        self.capacity += 1
        self.data += [None] * 1
        for i in reversed(range(len(self.data))):
            self.data[i] = self.data[i-1]
        self.data[0] = n
        self.size += 1

    def deleteend(self):
        n = len(self.data)
        del self.data[n - 1]

    def deletebeginning(self):
        del self.data[0]

    def deleteindex(self, n):
        del self.data[n]

    def deletevalue(self, n):
        self.data.remove(n)

    def elementbyindex(self, n):
        print(self.data[n])

    def updateelement(self, n, i):
        self.data[i] = n

    def search(self, x):
        for i in range(len(self.data)):
            if self.data[i] == x:
                print("Element ",x," exists at index", i)
                return
        print("Element not found")

    def maxi(self):
        c = self.data[0]
        for i in self.data:
            if i > c:
                c = i
        return c
    
    def mini(self):
        c = self.data[0]
        for i in self.data:
            if i < c:
                c = i
        return c
    
    def sums(self):
        c = 0
        for i in self.data:
            c = c + i
        return c
    
    def avg(self):
        s = self.sums()
        n = len(self.data)
        return s/n
    
    def count(self, n):
        c = 0
        for i in self.data:
            if i == n:
                c += 1
        return c

arr = Array(3)
print(arr.data)
arr.arrinsert(1)
arr.arrinsert(2)
arr.arrinsert(3)
print(arr.data)
arr.insertatend(4)
print(arr.data)
arr.insertatbeginning(5)
print(arr.data)
# arr.deleteend()
# print(arr.data)
# arr.deletevalue(2)
# print(arr.data)
arr.elementbyindex(0)
arr.updateelement(5, 2)
print(arr.data)
arr.search(9)
print(arr.maxi())
print(arr.mini())
print(arr.sums())
print(arr.avg())
print(arr.count(5))