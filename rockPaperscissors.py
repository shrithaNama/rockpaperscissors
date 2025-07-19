import random
print('========================')
print('========================')
print('welcome to rock paper and scissors')
print('========================')
print('========================\n\n')

print("1 is for '✊' (Rock).")
print("2 is for '✋' (Paper).")
print("3 is for '✌️' (Scissors).")

user=int(input('enter your choice: '))

if user==1:
    print ("you chose:'✊'")
elif user==2:
    print("'you chose:'✋'")
elif user==3:
    print("you chose:'✌️'")
else:
    print('invliad')
     
cpu=random.randint(1,3)
if cpu==1:
    print ("cpu chose:'✊'")
elif cpu==2:
    print("'cpu chose:'✋'")
elif cpu==3:
    print("cpu chose:'✌️'")
else:
    print("invalid")
    
def win(a,b):
    if a==b :
        print('tie')
    elif a==1 and b==2:
        print('cpu won')
    elif a==1 and b==3:
        print('user won')
    elif a==2 and b==1:
        print('user won')
    elif a==3 and b==1:
        print('cpu won')
    elif a==2 and b==3:
        print('cpu won')
    elif a==3 and b==2:
        print('user won')
    else:
        print('ntg')

win(user,cpu)
