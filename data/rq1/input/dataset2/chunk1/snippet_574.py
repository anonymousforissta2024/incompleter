#Source: https://stackoverflow.com/questions/70548682/python-for-loop-typeerror-int-object-is-not-iterable
heights = [165, 154, 156, 143, 168, 170, 163, 153, 167]
ages = [18, 16, 11, 34, 25, 9, 32, 45, 23]

heights_and_ages = list(zip(heights, ages))
heights_and_ages = [list(info) for info in heights_and_ages]

can_ride_coaster = []
for info in heights_and_ages:
  for height, age in info:
    if height > 161 and age > 12:
      can_ride_coaster.append(info)