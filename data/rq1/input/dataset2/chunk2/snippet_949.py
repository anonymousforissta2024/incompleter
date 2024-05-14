#Source: https://stackoverflow.com/questions/13832397/attributeerror-object-has-no-attribute-execute
def AddQuestion(self, Question, Answer1, Answer2, Answer3, Answer4):
    self.cursor.execute("""INSERT INTO questions
                        VALUES (?, ?, ?, ?, ?, ?)""", [None, Question, Answer1, Answer2, Answer3, Answer4, CorrectAnswer])
self.connection.commit()