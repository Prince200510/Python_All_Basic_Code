class Parent:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def set(self):
        print('===== Student Details =====')
        print('Name    :', self.name)
        print('Roll No :', self.roll_no)

name = str(input('Enter a Name        : '))
roll_no = int(input('Enter a roll number : ')) 

object = Parent(name, roll_no)
object.set()