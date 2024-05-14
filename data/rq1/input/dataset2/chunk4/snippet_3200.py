#Source: https://stackoverflow.com/questions/68671923/command-raised-an-exception-typeerror-str-object-does-not-support-item-delet
if str(user.id) in data:
        for element in data:
          if str(user.id) in element:
            del element[str(user.id)]