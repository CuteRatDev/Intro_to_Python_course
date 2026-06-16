while True:
    print("Tip calculator")
    totalBill = float(input("what is the total bill? \n"))
    percentBill = int(input("what is the percentage. 10 15 20 \n"))
    if not percentBill in [10, 15, 20]:
        print("your percentage is not in range")
    else:
        totalPeople = int(float(input("what is the total people? \n")))
    if 10 == percentBill:
        totalBill = (totalBill * 1.10)/totalPeople
        totalBill = round(totalBill, 2)
        print(f"Your bill is {totalBill}")
        break
    elif 15 == percentBill:
        totalBill = (totalBill * 1.15)/totalPeople
        totalBill = round(totalBill, 2)
        print(f"Your bill is {totalBill}")
        break
    elif 20 == percentBill:
        totalBill = (totalBill * 1.20)/totalPeople
        totalBill = round(totalBill, 2)
        print(f"Your bill is {totalBill}")
        break



