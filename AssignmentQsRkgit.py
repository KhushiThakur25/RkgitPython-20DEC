'''n = int(input("Enter the number"))
rev = 0
sums = 0
while n > 0:
    rev = rev*10 + 9
    print(rev)
    sums += rev
    n -= 1
print(sums)'''
n = 12345
n = str(n)
k = 2
while k >0:
    l = n[-1]
    mid = n[0:len(n)-1]
    n = l+mid
    k -= 1
print(n)
