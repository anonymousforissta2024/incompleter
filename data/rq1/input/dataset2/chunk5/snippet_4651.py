#Source: https://stackoverflow.com/questions/64691365/name-error-in-one-program-whereas-syntax-error-in-another
Z = (input("Enter a character: "))
if type(Z) == int:
   print(Z, "is a numeral")
else: 
   if (Z=='A' or Z=='a' or Z =='E' or Z=='e' or Z=='I'or Z=='i'
        or Z=='O' or Z=='o' or Z=='U' or Z=='u'):
      print(Z, "is a Vowel")
   else:
      print(Z, "is a Consonant")