class MyHashSet:
    # 復習

    def __init__(self):
        self.data = [[] for _ in range(1000)]

        

    def add(self, key: int) -> None:
        currkey = key % 1000

        if key not in self.data[currkey]:
            self.data[currkey].append(key)        
        

    def remove(self, key: int) -> None:
        currkey = key % 1000

        if key in self.data[currkey]:
            self.data[currkey].remove(key)  
        

    def contains(self, key: int) -> bool:
        currkey = key % 1000
        return key in self.data[currkey]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)