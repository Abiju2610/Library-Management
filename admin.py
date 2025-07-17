
from db import get_db_connection
from menu import Menu
import time

class Admin:
    def adminLogin(self):
        try:

            mydb = get_db_connection()
            mycursor = mydb.cursor()

            while True:
                user_input = input("Enter username (or type 'exit01' to quit): ")
                if user_input.lower() == 'exit01':
                    print("Exiting Login...")
                    return
                
                mycursor.execute("SELECT passwd FROM admin_lg WHERE username = %s", (user_input,))
                result = mycursor.fetchone()

                if result:
                    correct_password = result[0]

                    while True:
                        passwd = input("Enter Password: ").strip()
                        if passwd == correct_password:
                            print("Logging In...")
                            time.sleep(1)
                            view_menu = Menu()
                            view_menu.displayMenu()
                            return
                        else:
                            print("Wrong Password. Try again")
                else:
                    print("Incorrect Username. Try Again")

        except Exception as e:
            print(f"Error: {e}")
            
