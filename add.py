import sys
from db import get_db_connection

class AddBook:

    def get_next_book_id(self):
        try:
            """
            with open(filename, "r") as f:
                lines = f.readlines()

                if lines:
                    last_line = lines[-1].strip()
                    last_id = int(last_line.split(",")[0])
                    return last_id + 1
                else:
                    return 1000
                    """
            mydb = get_db_connection()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT ID FROM books ORDER BY ID DESC LIMIT 1")
            lastID = mycursor.fetchone()

            if lastID is not None:
                return lastID[0] + 1
            else:
                return 1000 

        except Exception as e:
            print("Error getting next book ID:", e)
            return 1000
        
    def add_book(self):
        book_name = input("\nEnter Book Name: ").strip()
        book_author = input("\nEnter Book Author: ").strip()

        next_id = self.get_next_book_id()

        """
        with open(filename, "a") as f:
            f.write(f"{next_id}, {book_name}, {book_author}\n")
        """

        mydb = get_db_connection()
        mycursor = mydb.cursor()
        
        sqlFormula = "INSERT INTO books (ID, book_name, book_author) VALUES (%s, %s, %s)"
        added_book = (next_id, book_name, book_author)

        mycursor.execute(sqlFormula, added_book)
        mydb.commit()

        print("\nBook added successfully...")
        self.continue_menu()


    def continue_menu(self):

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
