def menu():
    print("Math Menu")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("0. Exit")

def option1():
    print("You selected Option 1")

def option2():
    print("You selected Option 2")

def option3():
    print("You selected Option 3")

def main():
    while True:
        menu()
        choice = input("Make your selection: \n")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid, please try again!")

main()
