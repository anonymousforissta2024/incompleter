#Source: https://stackoverflow.com/questions/54002012/pythontypeerror-float-object-is-not-iterable
#Conditions
B = 0
G = 0
R = 0

for i in range(0,len(vetor_x)):

    if vetor_x[i] <= 500:
        vetor_xB[B] = list(vetor_x[i])
        vetor_yB[B] = list(vetor_y[i])
        B += 1

    elif vetor_x[i] <= 600:
        vetor_xG[G] = list(vetor_x[i])
        vetor_yG[G] = list(vetor_y[i])
        G += 1

    elif vetor_x[i] <= 700:
        vetor_xR[R] = list(vetor_x[i])
        vetor_yR[R] = list(vetor_y[i])
        R += 1

print('####### vetor_xB #######')
print(vetor_xB)
print('####### vetor_yB #######')
print(vetor_xB)
print('####### vetor_xG #######')
print(vetor_xG)
print('####### vetor_yG #######')
print(vetor_yG)
print('####### vetor_xR #######')
print(vetor_xR)
print('####### vetor_yR #######')
print(vetor_yR)