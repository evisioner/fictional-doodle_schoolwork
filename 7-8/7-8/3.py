import string
import random

letters=string.ascii_letters
nums='1234567890'
store=letters+nums
password=[]

limit=int(input('>'))

for i in range(limit):
    password.append(random.choice(store))

print(''.join(password))