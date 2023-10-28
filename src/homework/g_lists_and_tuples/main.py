#
import lists 

inventory = {}

def display():
     print("Inventory Menu\n")
     print("1 - Update or Add Item")
     print("2 - Remove Item")
     print("3 - Exit")
     print("4 - Check List Inventory")

def run_menu():
     display()
     option = str(input("Select option 1, 2, 3, or 4: "))
     while option not in ('1','2','3','4'):
          print("Invalid Option")
          option = str(input("Select option 1, 2, 3, or 4: "))
     run_option(option)  


def run_option(option):
     if option == '1':
          option_1()
     if option == '2':
          option_2()
     if option == '3':
          option_3()
     if option == '4':
          option_4()

def option_1():
     while True:
          widget = str(input("What do you want to add or update to inventory: "))
          while True:
               try:
                    quantity = int(input("Insert Quantity of this Item: "))
                    break
               except ValueError:
                    print("Not a valid Quantity")
          lists.add_inventory(inventory, widget, quantity)
          while True:
               again = str(input("Do you want to add or update another Item Y or N? : "))
               if again in ("Y",'y','yes','YES'):
                    break
               if again in ('N','n','no','NO'):
                    print("Returning to Main Menu\n")
                    break
               else:
                    print("Invalid")
          if again in ('N','n','no','NO'):
               run_menu()
               break
          
def option_2():
     while True:
          widget = str(input("What Item would you like to remove from inventory: "))
          y= lists.remove_inventory_widget(inventory, widget)
          print(f'{y}\n')
          while True:
                    again = str(input("Would you like to remove another Item Y or N? : "))
                    if again in ("Y",'y','yes','YES'):
                         break
                    if again in ('N','n','no','NO'):
                         print("Returning to Main Menu\n")
                         break
                    else:
                         print("Invalid")
          if again in ('N','n','no','NO'):
               run_menu()
               break
          
def option_3():
     while True:
          exit = input("Are you sure you want to exit? Y or N?: ")
          if exit in ('y','Y','yes','YES'):
               print('Exiting Program')
               break
          if exit in ('n','N','no','NO'):
               print("Returning to Main Menu\n")
               run_menu()
               break
          else:
               print("Invalid Option")

def option_4():
     print("\nThis is the list of your inventory.")
     for item in inventory.items():
          print(item)
     main_menu = None
     main_menu = str(input("Press enter to return to Main Menu"))
     if main_menu != None:
          print("Returning to Main Menu.\n")
          run_menu()

run_menu() 

          