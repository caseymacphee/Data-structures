class LinkedEntry(object):
    def __init__(self, key, val):
        self.value = val
        self.key = key
        self.next = None

    def getVal(self):
        return self.value

    def setVal(self, val):
        self.val = val

    def getKey(self):
        return self.key

    def next(self):
        return self.next

    def setNext(self, next):
        self.next = next

class HashMap(object):
    def __init__(self, size):
        self.TABLE_SIZE = size
        self.table = []
        for entry in xrange(self.TABLE_SIZE):
            self.table.append(None)


    def hash(self, key):
        if type(key) is not str:
            raise Exception("Hash only takes strings for keys")
        ord_sum = 0
        for char in key:
            ord_sum += ord(char)
        return ord_sum

    def set(self, key, val):
        if type(key) is not int:
            raise Exception("Key must be a number")
        else:
            adjusted_key = key % self.TABLE_SIZE - 1
            current = self.table[adjusted_key]
            if current is None:
                self.table[adjusted_key] = LinkedEntry(key, val)
            else:
                prev = current
                while current is not None:
                    prev = current
                    current = current.next
                prev.next = LinkedEntry(key, val)
            
    def get(self, key):
        current = self.table[key % self.TABLE_SIZE - 1]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
            


