#Source: https://stackoverflow.com/questions/69669751/typeerror-bool-object-is-not-subscriptable-with-while-loop
ITI1=3
ITI2=5
ITI3=7
ItiDurations = list(itertools.repeat(ITI1, 6))+list(itertools.repeat(ITI2,4))+list(itertools.repeat(ITI3,2))
def duplicate(testlist, n):
    return testlist*n
ValCong=['pos', 'neg']
StimValCong = duplicate(ValCong,6)
ActCong=['go', 'nogo']
ActionCong = duplicate(ActCong,6)
# Congruency list (cong=0, incong=1)
Cong = duplicate([0],12)
Conblock_1 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
Conblock_2 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
Conblock_3 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
Conblock_4 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
Conblock_5 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
Conblock_6 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
Conblock_7 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
Conblock_8 = pd.DataFrame(list(zip(ItiDurations,StimValCong,ActionCong,Cong)),columns=['ITI','StimVal', 'Action', 'Congruency'])
dictCon={1:Conblock_1, 2:Conblock_2, 3:Conblock_3, 4:Conblock_4, 5:Conblock_5, 6:Conblock_6, 7:Conblock_7, 8:Conblock_8}