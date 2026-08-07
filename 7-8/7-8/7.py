import string
import random

digits=string.digits
letters=string.ascii_letters
lower=string.ascii_lowercase
upper=string.ascii_uppercase
special=string.punctuation
store=digits+letters+special

password=[]
for i in range(3):
    password.append(random.choice(lower))
    password.append(random.choice(upper))
    password.append(random.choice(digits))
    password.append(random.choice(special))

    for o in range(6):
        password.append(random.choice(store))

    random.shuffle(password)

    print(''.join(password))
    
    password=[] #resets the password for next loop :3