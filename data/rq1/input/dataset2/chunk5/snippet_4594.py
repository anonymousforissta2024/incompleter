#Source: https://stackoverflow.com/questions/48646779/typeerror-cupcake-flour-missing-1-required-positional-argument-cu-flour-w
user = input("How many cookies do you want to make? ")

def cupcake_flour(cu_flour):
  cu_flour = user * 100 / 120

  print(cu_flour + "cups of flour")

def main(): 
   cupcake_flour()

main()  