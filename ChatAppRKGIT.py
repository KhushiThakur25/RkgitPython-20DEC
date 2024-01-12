import random
greetingIntent = ["hello","hi","hy","hlo","hey there","hello there","hey"]
chat = True
while chat:
    msg = input("Enter the message..")
    msg = msg.lower()
    if msg in greetingIntent:
        print(random.choice(greetingIntent),"user")
    elif msg == "bye":
        print("ok Bye")
        chat = False
    else:
        print("I don't understand..")
#hy,hi,hey,hlo,hello,hi there is ___,this side ___
