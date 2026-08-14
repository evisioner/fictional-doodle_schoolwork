import string
import random

digits=string.digits
letters=string.ascii_letters
lower=string.ascii_lowercase
upper=string.ascii_uppercase
special=string.punctuation
omit='lioO0I1'
store=digits+letters+special

for char in omit:
    store=store.replace(char, '')

password=[]
limit=int(input())

password.append(random.choice(lower))
password.append(random.choice(upper))
password.append(random.choice(digits))
password.append(random.choice(special))

for i in range((limit-4)):
    password.append(random.choice(store))

random.shuffle(password)

print(''.join(password))