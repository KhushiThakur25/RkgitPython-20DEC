file = open('data.txt','r')
#data = file.read()
#data = file.read(100)
#data = file.readline()
file.seek(50)
data = file.read()
print(data)
file.close()