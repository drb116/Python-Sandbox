from builtins import range

#Single line comment
""" Multiline
 Comment """

''' Or single quotes '''

# Quotes can be used interchangeably, so I don't need an escape sequence

print('"Hello"') #Demo flipping these around
print("cat "*4)

''' Methods must be defined in the code before they can be called'''

def printHi(count): #Variables are assigned types by default
    print(float(count/2)) #I can cast, the reverse of java
    ''' int, float'''

    for i in range(count): #Standard loop
        print("Hi")

#Variable assignment methods
a=1
a=b=c=4
d,e,f = 3,4,5

colors = ["blue","red"]

for color in colors:
    print(color)
    print(color[:2])


for i in range(2,10,2): #(start(inclusive), stop(not inclusive), increment)
    if i==6: #basic conditionals
        print(i)

printHi(d)

my_name = "jackson"
print(my_name[2]) #One letter
print(my_name[2:4]) #Includes 2, but not 4
print(my_name[2:]) #From 2 on
print(my_name[:4]) #Up to 4
