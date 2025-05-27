# Simple Stack
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
obj1 = Stack()
obj1.push(10)
obj1.push(20)
print('Popped Item :', obj1.pop())

# Perfect Stack with menu driven
class Stack1:
    def __init__(self):
        self.data = []
    
    def pushed(self, item):
        self.data.append(item)
    
    def poped(self):
        if self.data == []:
            print('Stack is Empty')
            return -1
        else:
            remove = self.data.pop()
            print("Remove from Stack :", remove)
    
    def display(self):
        if self.data == []:
            print('Stack is Empty')
            return -1
        else:
            print("Stack :", self.data)

stack = Stack1()

while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = int(input("Enter element to push: "))
        stack.pushed(item)
    elif choice == '2':
        stack.poped()
    elif choice == '3':
        stack.display()
    elif choice == '4':
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Please enter 1-4.")

