dic = {
    "one":"1",
     "two":"2",
     "three":"3",
     "four":"4",
     "five":"5",
     "six":"6",
     "seven":"7",
     "eight":"8",
     "nine":"9",
     "zero":"0"}

value = input("Enter your string").lower()

'''ele = value.split()
print(ele)
for i in ele:
    rev = " ".join(dic[i])
    print(rev)'''

res = " ".join(dic[ele] for ele in value.split())
print(res)
    
