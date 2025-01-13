

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
        
print(d.kind)                  # shared by all dogs
        
print(e.kind)                  # shared by all dogs
        
print(d.name )                 # unique to d
        
print(e.name)                  # unique to e
        

class Dog:  
    tricks = []

    def __init__(self, name): 
        self.name = name
        self.tricks = []  

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')  
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks) 
print(e.tricks)  



#Random Remarks


class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)



class Bag:
    def __init__(self):
        self.data = []
        print(self.data)

    def add(self, x):
        self.data.append(x)
        print(self.data)


    def addtwice(self, x):
        self.add(x)
        self.add(x)
        print(self.data)



#Inheritance

class DerivedClassName(Dog):

    print(d.tricks)
    


#Multiple Inheritance

#multiple base class

#Private Variables

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update 
    

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)






from dataclasses import dataclass

@dataclass #Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items. 
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
print(john.dept)

print(john.salary)



#Iterators  

for element in [1,2,3]:
    print(element)        #most container objects can be looped over using a for statement#use of iterators pervades and unifies Python.

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123":
    print(char)

for line in open("myfile.txt"):
    print(line, end='')



#Generators

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        

    for char in reverse('golf'):
        print(char)










#Generator Expressions


# sum(i*i for i in range(10))                 # sum of squares


# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# sum(x*y for x,y in zip(xvec, yvec))         # dot product


# unique_words = set(word for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

# data = 'golf'
# list(data[i] for i in range(len(data)-1, -1, -1))





# Sum of squares of numbers from 0 to 9
sum_of_squares = sum(i * i for i in range(10))  
print(f"Sum of squares: {sum_of_squares}")

# Dot product of two vectors
xvec = [10, 20, 30]
yvec = [7, 5, 3]
dot_product = sum(x * y for x, y in zip(xvec, yvec))  
print(f"Dot product: {dot_product}")

# Unique words from a page (assuming 'page' is a list of strings)
page = ["This is a sentence.", "This is another sentence."]
unique_words = set(word for line in page for word in line.split())  
print(f"Unique words: {unique_words}")

# Valedictorian (assuming 'graduates' is a list of student objects)
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

graduates = [Student("John", 3.9), Student("Jane", 3.8)]
valedictorian = max((student.gpa, student.name) for student in graduates)  
print(f"Valedictorian: {valedictorian}")

# Reversing a string (using list comprehension)
data = 'golf'
reversed_data = list(data[i] for i in range(len(data) - 1, -1, -1))
print(f"Reversed string: {reversed_data}")
