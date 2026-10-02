import random
random_num = random.randint(1,100)

new_num=int(input("enter your number: "))
print(new_num)
while new_num != random_num:
    if new_num < random_num:
        print("Your number is too low")
    else:
        print("Your number is too high")
    new_num=int(input("enter your number: "))
