#Source: https://stackoverflow.com/questions/54831355/how-to-fix-bcrypt-type-error-unicode-objects-must-be-encoded-before-hashing
import bcrypt 

password = input("Input your desired password: ")
hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())