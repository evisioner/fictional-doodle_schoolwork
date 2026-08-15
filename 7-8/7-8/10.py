import string
import random

digits=string.digits
letters=string.ascii_letters
lower=string.ascii_lowercase
upper=string.ascii_uppercase
special=string.punctuation
store=digits+letters+special

password=[]
number_of_passwords = 0
limit=0

while True:
    limit=int(input('how characters do you wnat your password to have (4 or more)'))
    if limit < 4:
        print('pls try again')
    else:
        break

while True:
    number_of_passwords=int(input('how many passwords do you want to generate'))
    if number_of_passwords <= 0:
        ans=input('does this mean u want 0 passwords?')
        if ans == 'yes':
            print('uh okay sure')
            exit(0)
        else:
            print('stop messing around and try again')
    else:
        break

for i in range(number_of_passwords):
    password.append(random.choice(lower))
    password.append(random.choice(upper))
    password.append(random.choice(digits))
    password.append(random.choice(special))

    for o in range(limit):
        password.append(random.choice(store))

    random.shuffle(password)

    print(f'your {i+1}(st/nd/rd/th) password is:', ''.join(password))
    
    password=[] #resets the password for next loop :3

if limit < 8:
    print('this password is weak')
elif limit >= 8 and limit < 12:
    print('this password is medium')
else:
    print('this password is strong')