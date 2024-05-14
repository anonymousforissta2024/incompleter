#Source: https://stackoverflow.com/questions/70164872/problems-in-the-use-of-sum-typeerror-int-object-is-not-iterable
#ELEMENT 1
cursor.execute('SELECT City FROM Nation WHERE X = ?', [X])
count_A = cursor.fetchall() #Print [(2,), (1,), (2,)]

sum_A = sum(int(row[0]) for row in count_A) #print 5
print(sum_A)
###########################################

#ELEMENT 2
cursor.execute('SELECT City FROM Nation WHERE Y = ?', [Y])
count_B = cursor.fetchall() #Print [(3,), (2,)]

sum_B = sum(int(row[0]) for row in count_B) #print 5
print(sum_B)
###########################################

SumA_B = sum(sum_A, sum_B) 
print(SumA_B) #ERROR: I would like to get result 10