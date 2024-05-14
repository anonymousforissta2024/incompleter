#Source: https://stackoverflow.com/questions/22664491/typeerror-unsupported-operand-types-for-float-and-str
import random
initial_val = str(10)
attr_c1_stre = ("Character 1's Strength: ",str(random.randint(1,12)/random.randint(1,4)     + initial_val))
attr_c1_skill = ("Character 1's Skill: ",str(random.randint(1,12)/random.randint(1,4) +     initial_val))
attr_c2_stre = ("Character 2's Strength: ",str(random.randint(1,12)/random.randint(1,4)     + initial_val))
attr_c2_skill = ("Character 2's Skill: ",str(random.randint(1,12)/random.randint(1,4) +     initial_val))
print("attr_c1_stre", "\nattr_c1_skil", "\n\nattr_c2_stre","\nattr_c2_skill")
file = open("Attribute.txt", "w")
file.write(attributes)
file.close()
input("\n\nPress enter to exit")