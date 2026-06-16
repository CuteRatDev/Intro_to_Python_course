while True:
    name = input("what is the name\n")

    has_digit = any(char.isdigit() for char in name)
    too_long = len(name) >= 10

    if not  has_digit and not too_long:
        name_length= len(name)
        name_result = name
        print(name)
        break

    if has_digit and too_long:
        print("your name is too long and cotains a digit")
    elif has_digit:
        print("Your name can not have a digit")
    elif too_long:
        print("your name needs to be shorter than 10")

print(f"Great to me you {name_result} your name is {name_length}")