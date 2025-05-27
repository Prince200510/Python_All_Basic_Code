class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        print(self.items)
        
    def dequeue(self):
        return self.items.pop()

obj1 = Queue()
obj1.enqueue(10)
obj1.enqueue(20)
obj1.enqueue(30)
obj1.enqueue(40)
print('Dequeue :', obj1.dequeue())
obj1.enqueue(50)
obj1.enqueue(60)
