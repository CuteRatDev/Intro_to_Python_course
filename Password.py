import random

password_min = input("Enter a min number: ")
while not password_min.isdigit():
    password_min = input("Please enter a min integer: ")
password_min = int(password_min)

password_max = input("Enter a max number: ")
while not password_max.isdigit():
    password_max = input("Please enter a max integer: ")
password_max = int(password_max)
while password_min > password_max or password_min == password_max:
    password_max = int(input("Please enter a number higher than " + str(password_min) + ": "))

q_let = input("Do you want letters? (y/n): ").lower()
while q_let not in ["y", "n"]:
    q_let = input("Please enter either Y or N: ").lower()

if q_let == "y":
    q_let = True
elif q_let == "n":
    q_let = False
else:
    q_let = "unset"


q_spec = input("Do you want special characters? (y/n): ").lower()
while q_spec not in ["y", "n"]:
    q_spec = input("Please enter either Y or N: ").lower()

if q_spec == "y":
    q_spec = True
elif q_spec == "n":
    q_spec = False
else:
    q_spec = "unset"


possible_num = ["0","1","2","4","5","6","7","8","9"]
possible_let = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z","A","B","C","D","E","F","G","H",]
possible_spec = ["!","@","#","$","%","^","&","*"]
possible_all = (possible_num + possible_let + possible_spec)

password_list =[]

possible_choice = "possible_none"
if q_let is True and q_spec is True:
    possible_choice = possible_all
elif q_let is False and q_spec is True:
    possible_choice = (possible_num + possible_spec)
elif q_let is True and q_spec is False:
    possible_choice = (possible_num + possible_let)
else:
    possible_choice = possible_num


for i in range(password_min, password_max + 1):
    password_list.append(random.choice(possible_choice))
random.shuffle(password_list)
password = ''.join(password_list)

print(f"your password is: {password}")

