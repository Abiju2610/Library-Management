class Menu:

    def systemMenuDisplay(self):
        width = 20

        print('-' * width)
        print(f"{'Menu':^{width}}") 
        print('-' * width)

        print(f"| {'(1) Add Books':<{width - 4}} |")
        print(f"| {'(2) View Books':<{width - 4}} |")
        print(f"| {'(3) Done':<{width - 4}} |")
        print('-' * width)

    

    def displayMenu(self):
        from add import AddBook
        from view import ViewBooks

        choice = ""
        menuDone = False

        while not menuDone:
            self.systemMenuDisplay()
            
            while choice != "1" and choice != "2" and choice != "3":
                choice = input("\nEnter either 1, 2 or 3: ")

            if choice == "1":
                add_book = AddBook()
                add_book.add_book("library.txt")

            elif choice == "2":
                view_books = ViewBooks()
                view_books.view_all_books("library.txt")
            else:
                menuDone = True