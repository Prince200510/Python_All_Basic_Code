class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        print(self.count)
    
    def decrement(self):
        self.count -= 1
        print(self.count)
    
    def reset(self):
        self.count = 0
        print(self.count)

obj = Counter()

while True:
    print('================')
    print('press 1 Increment')
    print('press 2 Decrement')
    print('press 3 Reset')
    print('press 4 Exit')
    
    choice = input('Enter your choice :')
    
    if choice == '1':
        obj.increment()
    elif choice == '2':
        obj.decrement()
    elif choice == '3':
        obj.reset()
    elif choice == '4':
        break
    else:
        print("Invalid input. Please try again.")