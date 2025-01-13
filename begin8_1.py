
f = open('workfile', 'w', encoding="utf-8")

#open() returns a file object , and is most commonly used with two positional arguments and one keyword argument 

with open ('workfile' , encoding = "utf - 8 ") as f:
    read_data =  f.read()
    print(read_data)

# We can check that the file has been automatically closed

    f.closed

    print('hi')


  
    # f.read() #after closing file object one cannot read .

    #Methods of File Objects

    f.readline()

    f.readline()

    f.readline()

    for line in f:
        print(line, end='')




import json
x = [1, 'simple', 'list']
json.dumps(x)
print(x)
