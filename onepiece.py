

def fight(): 
    print("\n~ mini game ~\n")


def list_of_skills() : 
        print("------List of Skills------")
        print("Power Level: __ \n\nb. Back\nf. Fight!")
        user_input = input("")

        if user_input == '1': 
            list_of_skills()
        elif user_input == 'b': 
            list_of_fighters()
        elif user_input == 'f': 
            fight()
        else: 
            print("please choose a slection from the menu")
            list_of_skills()

def list_of_fighters(): 
        print("-----List of Fighters-----")
        print("1. Luffy\n2. Zoro\nb. Back")
        user_input = input("")

        if user_input == '1': 
            list_of_skills()
        elif user_input == '2': 
            list_of_skills()
        elif user_input == 'b': 
            menu()
        else: 
            print("please choose a slection from the menu")
            list_of_fighters()

def menu() :

        print("\n\n--------menu--------")
        print("1. Choose your Fighter \n2. Add a new fighter\n3. Quit")

        menu_choice = input("")

        if menu_choice == '1': 
            list_of_fighters()
        elif menu_choice == '2': 
            print("2")
        elif menu_choice == '3': 
            return
        else: 
            print("please choose a slection from the menu")


def main() :

    username = input("Username:  ")

    menu()

    
if __name__ == "__main__":
    main()