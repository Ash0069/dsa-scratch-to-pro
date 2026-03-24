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
    
    def reverse(self):
        a = [None] * self.size
        for i in range(0, self.size):
            a[i] = self.data[(self.size-1) - i]
        return a
    
    def tworeverse(self):
        i = 0
        j = self.size - 1
        while i < j:
            l = self.data[i]
            self.data[i] = self.data[j]
            self.data[j] = l
            i += 1
            j -= 1
        return self.data
    
    def rotateleft(self, k):
        n = self.size
        if n==0:
            return self.data
        
        k = k % n
        res = [0] * n

        for i in range(n):
            res[i] = self.data[(i+k)%n]

        return res
    
    def rotateright(self, k):
        n = self.size
        if n==0:
            return self.data
        
        k = k % n
        res = [0] * n

        for i in range(n):
            res[i] = self.data[(i-k)%n]

        return res
    
    def binarysearchiterative(self, k, low, high):
        while low <= high:
            mid = low + (high-low)//2

            if self.data[mid] == k:
                print("Found")
                return mid
            elif k > self.data[mid]:
                low = mid + 1
            else:
                high = mid - 1

        print("Not found")
        return -1
    
    def binarysearchrecursive(self, k, low, high):
        if low > high:
            return -1
        
        mid = low + (high - low) // 2

        if self.data[mid] == k:
            print("found")
            return mid
        elif k > self.data[mid]:
            return self.binarysearchrecursive(k, mid + 1, high)
        else:
            return self.binarysearchrecursive(k, low, mid - 1)
        
    def removeduplicates(self):
        s =set()
        res = []
        for i in self.data:
            if i not in s:
                s.add(i)
                res.append(i)
            else:
                continue
        return res
    
    def removesorteduplicates(self):
        self.data = sorted(self.data)
        if self.size <= 1:
            return self.data
        
        res = [self.data[0]]
        l, r = 0, 1

        while r < self.size:
            if self.data[l] != self.data[r]:
                res.append(self.data[r])
                l = r
            r += 1
        return res 

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
arr.insertatend(6)
print(arr.data)
print(arr.rotateleft(2))
print(arr.rotateright(2))
arr.binarysearchiterative(3, 0, len(arr.data))
arr.binarysearchrecursive(1, 0, len(arr.data))
print(arr.removesorteduplicates())