def add(num_1,num_2):
    z = num_1 + num_2
    print(z)

def sub(num_1,num_2):
    z = num_1 - num_2
    print(z)

def mul(num_1,num_2):
    z = num_1 * num_2
    print(z)


'''print(""" 1. ADD
            2.SUBTRACT
            3.MULTIPLY
            """)'''
dicts = {
    "1":add,
    "2":sub,
    "3":mul}
ch = input("Enter your choice..")
num_1 = int(input("Enter the first no."))
num_2 = int(input("Enter the second no."))

dicts.get(ch)(num_1,num_2)

#lis[int(ch)-1](num_1,num_2)

'''if ch == "1":
    add(num_1,num_2)

elif ch == "2":
    sub(num_1,num_2)
elif ch == "3":
    mul(num_1,num_2)
else:
    print("Invalid choice..")'''
