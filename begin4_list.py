squares = [1,2,3,4]
print(squares)

print(squares[0])

print(squares[-2])

print(squares + [5,6,7,8,9,10])

cubes = [8,27,65,125] #unlike string lists are mutable
4**3
cubes[2] = 4**3
print(cubes)

cubes.append(216) #append is used to add cube of 6 or 7 
cubes.append(7**3)
print(cubes)

rgb = ["Red","Green","Blue"]# when u assign list to a variable , variable refers to the existing list
rgba = rgb
id(rgb)==id(rgba)
True
rgba.append("Alph")
print(rgb)

correct_rgba = rgba[:]
correct_rgba[-1] ='Alpha'
print(correct_rgba)
print(rgba) #slice operations return a new list containing the requested elements ,slice returns in to a shallow copy(assignment statements donot copy objects,they create bindings between target and  object)

letters = [ 'a','b','c','d','e','f','g']
print(letters)

letters[2:5] = ['C','D','E'] #replace some values
print(letters)

letters[2:5] = []
print(letters) #remove some values

letters[:] =[] #clear the list by replacing all elements with empty list.
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']   #nest list (create list containing other list )
n = [1, 2, 3]
x = [a, n]
print(x)

[ ['a', 'b', 'c'],[1, 2, 3]]
print(x[0])
print(x[0][1])


a,b = 0,1   #Fibonacci series (Each element is a summ of its preceeding element)

while a < 10 : 
    print(a)
    a, b = b, a+b
    print(b)
    print(a+b)

i = 256*256
print('The value of i is', i)


a, b = 0, 1
while a < 1000:
    print(a, end=',')#loop 0,0
    print(b)#0,1 loop
    a, b = b, a+b
    print(b)

