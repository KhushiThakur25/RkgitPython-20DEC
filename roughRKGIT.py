def calc():
    x = 6
    y = 5
    def add():
        z1 = x+y
        #print(z1)
        return z1
    def sub():
        z2 = x-y
        #print(z2)
        return z2
    return add,sub
    

a,b = calc()
print(a())


#lambda function
'''1. it is an anonymous function
2.use it without def keyword
3.it is a single line function
4.Syntax - lambda argument : expression'''

strs = "Brainmentors"

s = lambda x : x.upper()
print(s(strs))



        
