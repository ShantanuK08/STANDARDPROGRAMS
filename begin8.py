#Input and Output

#Fancier Output Formatting

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')


#sr format method needs more manual effort 


yes_votes = 42_572_654
total_votes = 85_705_149

percentage = yes_votes/total_votes


print('{:-9}Yes votes {:2.2%}'. format (yes_votes, percentage))



s = ' Hello ,World'

str(s)

repr(s)

str(1/7)


x = 10 * 3.25
y = 200 * 200

s = 'The value of x is' +  repr(x) +', and y is ' + repr(y) + '...'
print(s)


# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)




# The argument to repr() may be any Python object:
a = repr((x, y, ('spam', 'eggs')))

print(a)







#Formatted String Literals




import math
print(f'The value of pi is approximately {math.pi:.3f}.')



#passing an integer after the ':'  will cause that field to be a minimum number of characters wide .

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')




bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')


#The String format() Method


print('We are the {} who say "{}!"'.format('knights', 'Hi'))



print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))





#if keyword arguments are used in the str.formats () method , their values are referred to by using the name of name of the argument.
print('This {food} is {adjective} .' . format (food = 'spam' , adjective =' absolutely horrible'))



print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '     #This can be done by simply passing the dict and using square brackets '[]' to access the keys.
        'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)) # this could be done  by passing table dictionary as keyword argument 

table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
print(message.format(**table))   #This is particularly useful in combination with the built-in function vars(), which returns a dictionary containing all local variables:


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))






    #Manual String Formatting



    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
        print(repr(x*x*x).rjust(4))





a='12'.zfill(5)
print(a)


b='-3.14'.zfill(7)
print(b)
c='3.14159265359'.zfill(5)
print(c)


import math
print('The value of pi is approximately %5.3f.' % math.pi)






print= ('hi')
