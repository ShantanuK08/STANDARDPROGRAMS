
#A First Look at Classes


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hello World'
    
    #correct way 

# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         print('Hello World')

# # Create an instance of MyClass
# my_instance = MyClass()

# # Call the method f() on the instance
# my_instance.f()  # This will print "Hello World"




class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

print(x.r, x.i)
    

#Instance Objects


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


#Method Objects


# xf = x.f
# while True:
#     print(xf())


