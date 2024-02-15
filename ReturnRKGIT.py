'''def calc(x,y):
    z1 = x+y
    z2 = x-y
    z3 = x*y
    z4 = x/y
    return z1,z2,z3,z4

a,b,c,d = calc(3,4)
print(a)
print(b)
print(c)
print(d)'''

def calc():
    x = 6
    y = 7
    print("Start calc")
    def add():
        m = x+y
        print("Sum is :",m)
        return m
    def sub():
        n = x-y
        print("Sub is :",n)
        return n
    return add(),sub()
        
add,sub = calc()
print(add)
print(sub)
#print(add())
#print(sub())
