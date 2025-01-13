
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        print(x)
        print(y)


def where_is (point):

    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")



      




# Automatically executed test cases
for x, y in [(0, 0), (0, 5), (5, 0), (3, 4)]:
   where_is(Point(x, y))



class Points_1:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def where_is (points_1):

        match points_1 :
            case[]:
                print('no Points_1')

            case[Points_1(0,0)]:
                print('The Origin')

            case[Points_1(x,y)]:
                print(f"Single Point {x},{y}")

            case[Points_1(0,y1),Points_1(0,y2)]:
                print(f"Two on the Y axis at {y1},{y2}")

            case _:
                print("Something else")

# Example Usage
points = [
    Points_1(0, 0),
    Points_1(0, 5),
    Points_1(0, 10),
]

Points_1.where_is([Points_1(0, 0)])  # The Origin
Points_1.where_is([Points_1(2, 3)])  # Single Point 2,3
Points_1.where_is([Points_1(0, 5), Points_1(0, 10)])  # Two on the Y axis at 5,10
Points_1.where_is([])  # No Points_1
Points_1.where_is(points)  # Something else





from enum import Enum

class Color(Enum):
    Red = 'red'
    Green = 'green'
    Blue = 'blue'

color = Color(input("Enter your choice of 'red' , 'blue' or 'green' :  "))
match color : 
    case  Color.Red:
        print("I see read")
    case Color.Green:
        print("I see Green")
    case Color.Blue :
        print("I see Blue")


# Defining Functions


def fib(n):
    """" Print a fibonacci series less than n """


    a,b = 0,1 
    while a < n :
        print(a,end = '')
        a,b = b , a+b
        print()

# Now call the function we just defined:
fib(2000)



#Default Argument Values

def ask_ok(prompt,retries =1 ,reminder = 'Please try again!'):
    while True :
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)



def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100 )    


#Default Argument Values


#the in keyword.eg.

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

#makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. 

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


#Keyword Arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    # Calling the parrot function
    parrot(1000)
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")





def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# Call the function outside the function definition
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


#Function Examples

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)





def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# Valid Call 1
print(combined_example(1, 2, kwd_only=3))

# Valid Call 2
print(combined_example(1, standard=2, kwd_only=3))

#keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.

def foo(name, /, **kwds):       # example function definitions paying close attention to the markers / and *
    return 'name' in kwds

print(foo(1, **{'name': 2}) )  #consider this function definition which has a potential collision between the positional argument name and **kwds which has name as a key


# Arbitrary Argument Lists

def write_multiple_items(file, separator, *args): #least used option is to call a function using an arbitary function.
    file.write(separator.join(args))

    #these variadic arguments will be last in the list of formal parameters,beause they sccop  up all arguments that are passed to function.


def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))


#unpacking argument lists 

list(range(3,6))#normal call with separate argument

args = [3,6]
print(list(range(*args))) #call with arguments unpacked from a list 




def parrot (voltage,state = 'a stiff',action = 'voom'):
    print(" -- This  parrot wouldn't", action ,end =  '')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's",state,"!")

d = {"voltage":"four million","state":"bleedin'demised","action":"VOOM"}
print(parrot(**d)) #reverse situation occurs when the argument is already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments.
#for instance the built in , range() funtion expects separate start and stop arguments .If they are not separately , write the function call with with the * operator to unpack the arguments out of a list or tuple.

#lambda function used to create small anonymouas function 

def make_incrementor (n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(0))

print(f(1))






pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key = lambda pair : pair [1])
print(pairs)


# Documentation Strings


def my_function():
    """"
          Do nothing , But Document it !

          no,really it doesn't do anything
                
                            """
    
    pass 
print(my_function.__doc__)

#Function Annotations

def f(ham:str,eggs:str = 'eggs') :
    print("Annotations:",f.__annotations__ )

    print("Arguments:",ham,eggs)

    return ham + 'and' + eggs

print(f('spam'))









