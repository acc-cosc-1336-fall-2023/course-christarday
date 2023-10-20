
import dictionary

def display_custom_menu():
    print("DNA Analysis Menu")
    print("1 - calculate Matrix Distance")
    print("2 - Exit")

def run_menu():
    display_custom_menu()
    choice = str(input("Select choice 1 or choice 2: "))
    while choice not in ('1','2'):
        choice = str(input("Invalid Option, Select choice 1 or choice 2: "))
    run_choice(choice)

def run_choice(input):
    if input == '1':
        choice_1()
        
    if input == '2':
        choice_2()
    
    def choice_1():
        print("n\You selected choice 1")
    a = create_list()
    while True:
        try:

            b = dictionary.get_p_distance_matrix(a)
            b = dictionary.get_p_distance_matrix_for(a)
            break 
        except ValueError:

            print("DNA strings are not of equal length. Try again.")
            a = create_list() 
        print(f"this is the matrix distance of your list:")
        print("\nThe matrix distance of your list is:")
         
        for i in range(len(b)):
            print(b[i])
        print('Back to Main Menu, Select 1 to Try Again, Select 2 to Exit\n')
        run_menu()

def choice_2():
    print("\nYou selected to Exit")
    while True:
        exit = input("Are you sure you want to exit? Y or N?: ")
        if exit in ('y', 'yes', 'Y', 'YES'):
            print('Exiting Program')
            break
        if exit in ('n', 'no', 'N', 'NO'):
            print("Returning to Main Menu\n")
            run_menu()
            break
        else:
            print("Invalid Choice")

def create_list():
    data = []
    while True:
        try:
            n = int(input("Enter the total amount of lists you want to find the matrix distance from: "))
            if n >= 1:
                break
            else:
                print("choose at least 1 or more")
        except ValueError:
            print("Not a whole number")
    print(f"Enter your {n} lists, SEPARATE strings with commas")
    for i in range(n):
        user_string = input(f"List No.{i+1}: ")
        user_list = user_string.split(',')
        data.append(user_list)

    return data
run_menu 

        
        
        