from add import AddBook

class ViewBooks:
    
    def view_all_books(self, filename):
        
        try:
            with open(filename, "r") as f:
                lines = f.readlines()

                width = 70

                print("-" * width)
                print(f"| {'BookId':<15} | {'Book name':<25} | {'Author':<20} |")
                print("-" * width)

                for line in lines:
                    values = [v.strip() for v in line.strip().split(',')]
                    if len(values) >= 3:
                        print(f"| {values[0]:<15} | {values[1]:<25} | {values[2]:<20}")
                    
                print("-" * width)
        
        except FileNotFoundError:
            print("Library file not found")

        
        view_menu = AddBook()
        view_menu.continue_menu()
