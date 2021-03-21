import os


def main():
    choice = input(
        "To open Videos (Enter: V). To open chrome (Enter: C): ")

    if choice == "V":
        os.system("explorer")
        os.startfile("D:")
        exit
    elif choice == "C":
        os.system("explorer")
        os.startfile(
            "C:\Program Files (x86)\Google\Chrome\Application")
        exit
    else:
        print("Please enter a valid choice")
        exit


if "__main__" == "__main__":
    main()
