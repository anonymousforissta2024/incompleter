#Source: https://stackoverflow.com/questions/54479475/how-to-fix-typeerror-str-object-is-not-callable
import uuid
import hashlib
login_or_signup = input("would you like to log in? Or signup?: ")

if login_or_signup("signup"):
  def hash_password(password):
      # uuid is used to generate a random number
      salt = uuid.uuid4().hex
      return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

  def check_password(hashed_password, user_password):
      password, salt = hashed_password.split(':')
      return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

  new_pass = input('Please enter a password: ')
  hashed_password = hash_password(new_pass)
  old_pass = input('Now please enter the password again to check: ')
  if check_password(hashed_password, old_pass):
      print('The passwords match!')
  else:
      print('I am sorry but the password does not match')

else:
  print("(NOT CODED YET)")