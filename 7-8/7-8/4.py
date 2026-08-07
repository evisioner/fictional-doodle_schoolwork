import random

go=[]
rand='1234567890'

for i in range(5):
    go.append(random.choice(rand))
    
print(go)