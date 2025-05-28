class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        print('Inserted :', item)
    
    def dequeue(self):
        if self.items == []:
            print('Queue is Empty')
        else:
            data = self.items.pop()
            print('Dequeue :', data)
    
    def display(self):
        if self.items == []:
            print('Queue is Empty')
        else:
            print("Queue :", self.items)

obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.dequeue()
obj.enqueue(40)
obj.enqueue(50)
obj.display()