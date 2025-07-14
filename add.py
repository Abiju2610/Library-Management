import sys

class AddBook:
    with open("library.txt", "a") as f:
        pass

    def get_next_book_id(self, filename):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()

                if lines:
                    last_line = lines[-1].strip()
                    last_id = int(last_line.split(",")[0])
                    return last_id + 1
                else:
                    return 1000
        except FileNotFoundError:
            return 1000
        
    def add_book(self, filename):
        book_name = input("\nEnter Book Name: ").strip()
        book_author = input("\nEnter Book Author: ").strip()

        next_id = self.get_next_book_id(filename)

        with open(filename, "a") as f:
            f.write(f"{next_id}, {book_name}, {book_author}\n")

        print("\nBook added successfully...")
        self.continue_menu()


    def continue_menu(self):
        """
        to_menu = ""

        while to_menu != "y" and to_menu != "Y" and to_menu != "n" and to_menu != "N":
            to_menu = input("\nWould you like to continue to the main menu (y/n): ")
        
        if to_menu.lower == "y":
            self.add_menu
        """

        while True:
            to_menu = input("\nWould you like to continue to the main menu (y/n): ").strip().lower()
            if to_menu == "y":
                self.add_menu()
                break
            elif to_menu == "n":
                print("Exiting... Goodbye!")
                sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")




    def add_menu(self):
        from menu import Menu
        main_menu = Menu()
        main_menu.displayMenu()
