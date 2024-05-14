#Source: https://stackoverflow.com/questions/35280588/typeerror-execute-got-an-unexpected-keyword-argument-multi
query = "DELETE FROM Service_Machine WHERE Id=(SELECT Id FROM Machines WHERE Id="+id+");" \
        "DELETE FROM Machine_Usage WHERE Id=(SELECT Id FROM Machines WHERE Id="+id+");" \
                    "DELETE FROM Machines WHERE Id="+id+");"
print(query)
self.cursor.execute(query, multi=True)