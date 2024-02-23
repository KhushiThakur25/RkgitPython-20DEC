#if file already exist then it throw error..abs
file = open('data_1.txt','x')
data = "Python was conceived in the late 1980s[40] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language"
file.write(data)
file.close()