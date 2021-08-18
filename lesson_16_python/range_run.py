number = input("PLease enter an integer: ")

if not number.isdecimal():
    print("Invalid input... Must number")
    exit(1)

for i in range(int(number), -1, -2):
    print(i)
