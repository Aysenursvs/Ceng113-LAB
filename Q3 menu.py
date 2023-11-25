def addition():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter your number: "))
    result = num1 + num2
    return result

def subtraction():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter your number: "))
    result = num1 - num2
    return result

def multiplication():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter your number: "))   
    result = num1 * num2 
    return result

def division():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter your number: "))
    result = num1 / num2
    return result

def max():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter your number: "))
    if num1 > num2:
        return num1
    else:
        return num2
    
def min():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter your number: "))
    if num1 < num2:
        return num1
    else:
        return num2
    
calculate = input("Do you want to calculations? (y/n): ")

while calculate == "y":
    print("### MENU ### ")
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4- Division")
    print("5- Max value")
    print("6- Min value")
    print("7- Exist")

    choice = int(input("Enter your choice: (1, 2, 3, 4, 5, 6, 7)"))

    if choice == 1:
        print(addition())
    elif choice == 2:
        print(subtraction())
    elif choice == 3:
        print(multiplication())
    elif choice == 4:
        print(division())
    elif choice == 5:
        print(max())
    elif choice == 6:
        print(min())
    else:
        print("END")
        break

    calculate = input("Do you want to calculations? (y/n): ")

