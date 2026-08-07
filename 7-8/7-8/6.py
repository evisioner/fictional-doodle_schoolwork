import string
import random

digits=string.digits
letters=string.ascii_letters
lower=string.ascii_lowercase
upper=string.ascii_uppercase
special=string.punctuation
store=digits+letters+special

password=[]
while True:
    limit=int(input())
    if limit < 4:
        print('pls try again')
    else:
        break

password.append(random.choice(lower))
password.append(random.choice(upper))
password.append(random.choice(digits))
password.append(random.choice(special))

for i in range((limit-4)):
    password.append(random.choice(store))

random.shuffle(password)

print(''.join(password))