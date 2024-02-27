# Exception Handling
# 1.try-logic
# 2.except-error
# 3.else-option
# 4.finally-I'm always executed...

try:
    num_1 = int(input("Enter the first value"))
    num_2 = int(input("Enter the second value"))

    add = num_1 + num_2
    sub = num_1 - num_2
    div = num_1/num_2


except ValueError:
    print("Please enter the valid input..")
except ZeroDivisionError:
    print("zero value can't divides the value.. ")
except Exception as msg:
    print(msg)
else:
     print("Sum is",add)
     print("Sub is",sub)
     print("Div is",div)
finally:
    print("I'm always executed...")
    