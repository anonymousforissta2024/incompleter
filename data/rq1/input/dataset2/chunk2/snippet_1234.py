#Source: https://stackoverflow.com/questions/68279152/tkinter-button-attributeerror-when-trying-to-use-a-class-method-for-the-comman
class SelectUserPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
    
        # Create label which instructs user how to select their profile
        instruct_label = tk.Label(self, text = "Enter your username from the records below")
        instruct_label.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    
        # Create text entry box with which the user can enter their username
        username_entry_label = tk.Label(self, text = "Username").grid(row = 1, column = 0, 
padx = 5)
        self.username_entry = tk.Entry(self, width = 30)
        self.username_entry.grid(row = 1, column = 1)
    
        # Create a button which can be used to select a user once username has been entered
        select_button = tk.Button(self, text = "Select User", width = 30, borderwidth = 
                                  BTN_BORD_WIDTH,
                                  command = self.select_user)
        select_button.grid(row = 2, column = 0, columnspan = 2, pady = (15, 5))
    
        # Create a back button
        back_button = tk.Button(self, text = "Back", width = 30, borderwidth = BTN_BORD_WIDTH,
                                command = lambda: master.change_frame(LoginPage))
        back_button.grid(row = 3, column = 0, columnspan = 2, pady = 5)
    
        # Display stored user records
        conn = sql.connect("application data/database.db")
        c = conn.cursor()
    
        c.execute("SELECT * FROM user_info")
        records = c.fetchall()
    
        conn.commit()
        conn.close()
    
        username_col = "Username" + "\n"
        user_ID_col = "User_ID" + "\n"
        for record in records:
            username_col += str(record[0]) + "\n"
            user_ID_col += str(record[1]) + "\n"
    
        usernames_label = tk.Label(self, text = username_col)
        usernames_label.grid(row = 4, column = 0, pady = 10)
    
        user_ID_label = tk.Label(self, text = user_ID_col)
        user_ID_label.grid(row = 4, column = 1, pady = 10)
    
        # Configure frame to horizontally centre widgets
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
    
        # Create function which selects a user if they exist in the records
        def select_user(self):
            username = self.username_entry.get()
            if username == "":
                return
        
            conn = sql.connect("application data/database")
            c = conn.cursor()
        
            c.execute("SELECT username, user_ID FROM user_info")
            records = c.fetchall()
        
            for record in records:
                if record[0] == username:
                    master.username == username
                    master.user_ID == record[1]
                
                    c.close()
                
                    master.change_frame(HomePage)
                
            self.username_entry.delete(0, tk.END)
            return