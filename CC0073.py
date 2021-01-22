result = 0
n = input("Enter a number to check whether it is an Armstrong number: ")
while n.isdigit() != True or int(n) == 0:
    n = input("It is an invalid entry. Don't use non-numeric, float, or negative values!: ")

if n.isdigit() == True and int(n) != 0:
    for i in n:
        result += int(i) ** len(n)
    if int(n) == result:
        print(f"Well Done! {n} is an Armstrong number!")
    else:
        print(f"Sorry! {n} is not an Armstrong number!")
