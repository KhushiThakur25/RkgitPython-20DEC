number = 65
print("Our number is",number)
print("Our number is",number,sep = "->")
print("Our number is",number,end=" ")
print("Hello world...")
x = 10
y = 20
div = x/y
print("div is:",div)
#walrus operator..
print("Sum is",z := x+y)
#printing methods:
print("sum of", x ,"and", y ,"is:",z)
print("Div of %d and %d is:%f"%(x,y,div))

print("Div of {} and {} is {}".format(y,x,div))
print("Div of {1} and {0} is {2}".format(y,x,div))
#f-string method...
print(f"Div of {x} and {y} is {div}")

#input in python
val_1 = int(input("Enter the first value.."))
val_2 = int(input("Enter the second value.."))
print(val_1+val_2)
