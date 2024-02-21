def  temp_convert(c):
    return 9/5*c + 32

def km_to_m(km):
    return km*1000

temp = [32.5,65.21,45.3,96.1,74.5,54.6]
kms = [122,566,32,14,54,89,96]

'''f = []
for t in range(len(temp)):  
    f.append(temp_convert(temp[t]))

print(f)

m = []
for km in range(len(kms)):  
    m.append(km_to_m(kms[km]))

print(m)'''

'''def my_map(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data'''

print(list(map(temp_convert,temp)))
print(list(map(km_to_m,kms)))
