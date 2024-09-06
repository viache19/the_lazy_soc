import services
def show_menu():
    print("___________.__             .____                             _________________  _________")
    print("\__    ___/|  |__   ____   |    |   _____  ___________.__.  /   _____/\_____  \ \_   ___ \ ")
    print("  |    |   |  |  \_/ __ \  |    |   \__  \ \___   <   |  |  \_____  \  /   |   \/    \  \/")
    print("  |    |   |   Y  \  ___/  |    |___ / __ \_/    / \___  |  /        \/    |    \     \____")
    print("  |____|   |___|  /\___  > |_______ (____  /_____ \/ ____| /_______  /\_______  /\______  /")
    print("                \/     \/          \/    \/      \/\/              \/         \/        \/")
    print("")
    print("Select an Option:")
    print("1. option 1")
    print("2. option 2")
    print("3. option 3")
    print("4. Exit")

def execute_option(option):
    if option == 1:
        services.print_information()
        input("Press Enter to reload")
    elif option == 2:
        print("Has elegido la option 2")
    elif option == 3:
        print("Has elegido la option 3")
    elif option == 4:
        print("Saliendo del programa...")
    else:
        print("Not valid input, please select the options")

def menu():
    option = 0
    while option != 4:
        show_menu()
        try:
            option = int(input("Select the option: "))
            execute_option(option)
        except ValueError:
            print("Not valid input, please select the options")
