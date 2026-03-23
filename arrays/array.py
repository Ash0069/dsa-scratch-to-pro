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
arr.deleteend()
print(arr.data)
arr.deleteindex(2)
print(arr.data)