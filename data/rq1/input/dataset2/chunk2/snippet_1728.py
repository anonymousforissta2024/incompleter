#Source: https://stackoverflow.com/questions/75229680/problem-in-class-when-use-dictionary-attributeerror-my-data-object-has-no-at
class Page1(tk.Frame):
    def __init__(self, master, other, **kw):
        super().__init__(master, **kw)
        self.configure(bg='white')

        class My_Data():
            def __init__(self, Name, Year, Other):
                self.Name: str
                self.Year: float
                self.Other: float
                
        def function1(self):
            My_Dictionary = {}
            x = cursor.execute("sql")

            for row in x.fetchall():
                if row[0] not in My_Dictionary:
                    Data = My_Data(
                        Name=row[1],
                        Year=row[2],
                        Other=list())

                    My_Dictionary[row[0]] = info
                My_Dictionary[row[0]].Other.append(row[3])