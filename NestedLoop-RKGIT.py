'''n = 56
m = n//2
for i in range(2,m+1):
    if n%i == 0:
        print("number is not prime")
        break
else:
    print("number is prime")'''
n = 32
b = 65
t = 21
'''if n%2 == 0:
    print("even")
else:
    print("odd")'''
'''if n > b and n > t:
    print("n is greatest..")
elif b > n and b > t:
    print("b is greatest..")
else:
    print("t is greatest..")'''
result = "even" if n%2 == 0 else "odd"
print(result,"number")
