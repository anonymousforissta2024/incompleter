#Source: https://stackoverflow.com/questions/60888178/whats-wrong-with-my-python-about-typeerror-not-supported-between-instance
from ipywidgets import interact_manual
def BMI(height, weight):
    height = (float(height) / 100)**2
    weight = float(weight)
    BMI = weight/height
    print('Your BMI is {:.2f}'.format(BMI))

interact_manual(BMI, height='Please enter your height', weight='Please enter your weight')

if BMI<18.5:
    print('Eat more!')
elif BMI != 24:
    print('Take care of your health, eat less')
else:
    print('Nice:)')