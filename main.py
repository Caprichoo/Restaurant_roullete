import random
names = input("Enter your food partners names here, seperated by ','\n").split(',')
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
who_will_pay = names[random_choice]
print(f'The person who pays is {who_will_pay}')
