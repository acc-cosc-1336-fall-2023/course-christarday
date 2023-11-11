import class_a

def main():
    user_input = str(input("Press Y to roll a die and see the result: ")).lower()
    while user_input == 'y':
        my_die = class_a.die()
        my_die.roll()
        print("You rolled a", my_die.get_rolled_value())
        user_input = str(input("Press Y to roll the die again: ")).lower()
        print()

if __name__ == '__main__':
    main()