class MyHashMap:

    def __init__(self):
        self.capacity = 1000  
        self.data = [[] for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i in range(len(self.data[index])):
            k, v = self.data[index][i]
            if k == key:
                self.data[index][i] = (key, value)
                return
        self.data[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        for k, v in self.data[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for i in range(len(self.data[index])):
            k, v = self.data[index][i]
            if k == key:
                self.data[index].pop(i)
                return

        

