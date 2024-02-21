def even(num):
    return num%2 == 0
def odd(num):
    return num%2 != 0

'''print(even(32))
print(odd(33))'''

numbers = [56,23,89,74,15,12,21,64,55,79,20]
'''ev = []
od = []

for i in range(len(numbers)):
    if even(numbers[i]):
        ev.append(numbers[i])

    elif odd(numbers[i]):
        od.append(numbers[i])

print(ev)
print(od)'''

print(list(filter(even , numbers)))
print(list(filter(odd , numbers)))

#Lambda -keyword it is used to create single line function....

print(list(map(lambda x: x**2,numbers)))
