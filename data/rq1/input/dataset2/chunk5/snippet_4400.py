#Source: https://stackoverflow.com/questions/55094961/typeerror-unsupported-operand-types-for-nonetype-and-nonetype
def askuser(prompt):
  userAnswer = None
  while userAnswer is None:
    try:
      userAnswer = float(input("Enter: " + prompt + ":"))
      if userAnswer < 0:
        userAnswer = None
        raise ValueError
    except:  
      print("Number must be greater than 0.")
      return userAnswer

def calcm(male,female):
  return (male / male + female) * 100

def calcf(female,male):
  return (female/ male + female) * 100

def diplay(percent_female,percent_male):
  print("Percent of Females is: ", percent_female)
  print("Percent of Males is: ", percent_male)

def main():
  number_females = askuser("number of females")
  number_males = askuser("number of males")

  percent_female = calcf(number_males,number_females)
  percent_male = calcm(number_males,number_females)

  display(percent_male,percent_female)


main()