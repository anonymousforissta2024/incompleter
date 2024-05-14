#Source: https://stackoverflow.com/questions/46158510/nameerror-on-line-8-if-button-a-is-pressed
start = 0
ind = 0
ind1 = 5
c = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [], '20': []}
d  = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}
#Registering#
if button_a.is_pressed:
    start=1
    display.scroll("Index No.")
elif button_b.is_pressed:
    start=0


    if start==1: 
        rgs=''
        ind=0
        while True:
            rgs=''
            while rgs=='':
               display.scroll("Password")
               for i in range(8):
                   if button_a.is_pressed:
                       rgs+='0'
                   elif button_b.is_pressed:
                       rgs+='1'
               for j in range(20):
                   if c[j][1]==rgs:
                       rgs=''
                       display.scroll("PASSWORD USED")
                   else:
                       for q in range(20):
                           if c[q]==ind:
                               c[q][1]=rgs
                           display.show("OK")