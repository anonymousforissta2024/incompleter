#Source: https://stackoverflow.com/questions/65325108/i-keep-getting-a-type-error-got-str-instead-of-int
import pickle
usernames_passwords = open("username_password.pck", "wb")
customer_login = []
pickle.dump(customer_login, usernames_passwords, "wb")
usernames_passwords.close()