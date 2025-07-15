from add import AddBook
from db import get_db_connection

class ViewBooks:
    
    def view_all_books(self):
        
        try:
            mydb = get_db_connection()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT ID, book_name, book_author FROM books")
            results = mycursor.fetchall()


            width = 70

            print("-" * width)
            print(f"| {'BookId':<15} | {'Book name':<25} | {'Author':<20} |")
            print("-" * width)

            for row in results:
                book_id, book_name, book_author = row
                print(f"| {book_id:<15} | {book_name:<25} | {book_author:<20} |")
                    
            print("-" * width)
            mydb.close()
        except Exception as e:
            print(f"Error: {e}")

        
        view_menu = AddBook()
        view_menu.continue_menu()
