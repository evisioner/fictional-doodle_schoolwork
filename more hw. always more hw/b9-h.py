import random
import string

num=int(input())

digits='0987654321'
chars=string.ascii_letters+digits+string.punctuation

for i in range(num):
    print(random.choice(chars),end='')