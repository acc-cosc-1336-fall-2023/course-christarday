def get_factorial(num):
    product = 1
    if num < 0:
        return "Invalid, you can't factorial a negative number."
    else:
        for n in range(1, num+1):
            product *= n
        return product

def sum_odd_numbers(num):
    sum = 0
    counter = 0
    while counter < num:
        counter += 1
        if counter % 2 == 1:
            sum += counter

    return sum

def display_menu():
    print("Homework Menu 3")
    print("1 - Factorial")
    print("2 - Sum odd numbers")
    print("3 - Exit")

def run_menu():
    display_menu()
    option = input("Select your option 1, ,2, or 3: ")
    run_menu_option(option)

def run_menu_option(option):
    if(option == '1'):
        option_1_selected()
    if(option == '2'):
        option_2_selected()
    if(option == '3'):
        option_3_selected()

def option_1_selected():
    num = 0
    while num < 1 or num > 9:
        while True:
            try:
                num = int(input("Enter an number 1 to 9: "))
                break
            except ValueError:
                print("That is not a number, please input a number 1-9: ")

    factorial = get_factorial(num)
    print("The factorial of ",num,"is equal to: ",factorial)
    exit_menu()

def option_2_selected():
    num = 0
    while num < 1 or num > 99:
        while True:
            try:
                num = int(input("Enter a choice that is greater than 0 and less than 100: "))
                break
            except ValueError:
                print("That is not a number, please enter a number 1 to 99: ")
    sum = sum_odd_numbers(num)
    print("The sum of odd numbers for",num,"is:",sum)
    exit_menu()

def option_3_selected():
    while True:
        exit = input("Enter y if you want to exit, enter n if you want to continue")
        if exit == "y" or exit == "Y":
            print("Exiting Program")
            break
        elif exit == "n" or exit == "N":
            run_menu()
            break
        else:
            print("Enter Y or N")

def exit_menu():
    while True:
        continued = input("Do you want to continue Y or N: ")
        if continued == "Y" or continued == 'y':
            run_menu()
            break
        if continued == "N" or continued == "n":
            print("Exiting Program")
            break
        else:
            print("Enter either Y or N")

         

