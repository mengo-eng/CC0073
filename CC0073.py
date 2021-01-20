result = 0
n = input("Enter a number to check whether it is an Armstrong number: ")
while n.isdigit() != True or int(n) == 0:
    n = input("That wasn't an integer. Please, enter positive integer. ")
    if n.isdigit() == True and int(n) != 0:
        for i in n:
            result += int(i) ** len(n)
        if int(n) == result:
            print(f"Congratulation! {n} is an Armstrong number!")
        else:
            print(f"Sorry! {n} is not an Armstrong number!")
        break
else:
    print(n)