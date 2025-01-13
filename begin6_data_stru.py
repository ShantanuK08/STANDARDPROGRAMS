
# MORE ON LIST 

#list.append(x) : Add an item to the end of the list , so a[len(a):] = [x]

#list.extend(iterable): Extend the list from all items  from the iterable ,so  a[len(a):] = iterable

#list.insert (i,x): Insert an item at a given position . First argument is the index of the element of the element before which to insert ,so a.insert(0,x) inserts at the front of the lists , and a.insert(len(a),x) is a equivalent to a.append(x).

#list.remove(x): Remove the first from list whose value is equal to x. It raises value error if there is no such item.

#list.pop[(i)]: Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

#list.clear():Remove all items from the list. Similar to del a[:].

#list.index(x[, start[, end]]): Return zero based index in the list of the first item whose value is equal to x. 
# Raises a ValueError if there is no such item.
#The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

#list.count(x):Return the no. of times x appears inthe list.

#list.sort(*,key=None, reverse=False)
#sort the items of the list in the place (the arguments can be used for sort customization, see sorted() for their explanation).

#list.reverse():  Reverse the elements of the list in place.

#list.copy(): Return a shallow copy of list .



#Eg. of above 

fruits = ['orange','apple','banana','pear','kiwi','apple','banana']

print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 3))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)


fruits.pop()
print(fruits)





#Using Lists as Stacks


stack = [3,4,5]
stack.append(6)  #to add 
stack.append(7)

print(stack)

stack.pop()    #to remove

stack.pop()

print(stack)



# Using Lists as Queues



from collections import deque

from click import File

queue = deque (["Eric", "John", "Michael"])

queue.append("Terry") # Terry arrives
print(queue)

queue.append("Graham")# Graham arrives
print(queue)

queue.popleft()
'Eric'
print(queue)
queue.popleft()
'John'
print(queue)



#List Comprehensions



squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


square = list(map(lambda x: x**2, range(10)))

print(square)

squ = [x**2 for x in range(15)]
print(squ)


print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])   #For example, this listcomp combines the elements of two lists if they are not equal:


combs = []
for x in [1,2,3]:
    for y in [3,1,4,5]:
        if x != y:
            combs.append((x, y))

print(combs)


vec = [-4, -2, 0, 2, 4]

print([x*2 for x in vec])

print([x for x in vec if x>=0])

print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']       ## call a method on each element
print([weapon.strip() for weapon in freshfruit])

print([(x,x**2) for x in range (6)] )# create a list of 2-tuples like (number, square)


vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])




from math import pi
print([str(round(pi, i)) for i in range(1, 6)])


#Nested List Comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)



print([[row[i] for row in matrix ] for i  in range(4)])

transposed = []
for i in range(4):
    transposed.append ([row [i] for row in  matrix])

    print(transposed)


transposed = []
for i in range (4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


    print(transposed)




#in real world on should prefer zip() function to complex flow statements.

print(list(zip(*matrix)))



#The del statement

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)




#Tuples and Sequences


t = 12345, 54321, 'hello!'
t[0]

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)


# Tuples are immutable:
#t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)



empty = ()
singleton = 'hello'
print(len(empty))


len(singleton)

print(singleton)



t = 12345, 54321, 'hello!'

x, y, z = t

print(x)

print(y)

print(z)

#Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  

print('orange' in basket)  

print('crabgrass' in basket)



# Demonstrate set operations on unique letters from two words


a = set('abracadabra')
b = set('alacazam')


print(a)                                  # unique letters in a

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print (a ^ b )                             # letters in a or b but not both





a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


#Dictionaries


tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127

print(tel)


del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

'guido' in tel

'jack' not in tel




print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))



print({x: x**2 for x in (2, 4, 6)})


print(dict(sape=4139, guido=4127, jack=4098))


#Looping Techniques



knights = {'gallahad': 'the pure', 'robin': 'the brave'} #items method - Return a new view of the dictionary’s items ((key, value) pairs). 
for k, v in knights.items():#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
    print(k, v)



for i,v in enumerate(['tic', 'tac', 'toe']): #when looping through a sequence ,the position index and corresponding value can be retrieved at the same time using then enumeratrea() function.
    print(i, v)



#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q ,a in zip(questions,answers):
    print('What is your {0}? It is {1} .' .format(q,a))


for i in reversed(range(1, 10, 2)):#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'] #To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
for i in sorted(basket):
    print(i)

#It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

import math
raw_data = [56.2 , float ('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8 ]

filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

# More on Conditions

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)




print((1, 2, 3)              < (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))



