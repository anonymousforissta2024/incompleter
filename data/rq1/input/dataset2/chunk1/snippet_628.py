#Source: https://stackoverflow.com/questions/64550556/picklingerror-could-not-serialize-object-typeerror-cant-pickle-jpype-jmeth
rdd.take(3)
'''
[Row(practiceid=701, dosequantity='200', dosefrequency='take 2 tablet by oral route  every day', count_dosequantity=716, count_dosefrequency=1, count_patientuid=306, DM Current -hychqudose='200mg', DM Expected Value='400mg'),
 Row(practiceid=595, dosequantity='200', dosefrequency='take 1 tablet by oral route 2 times every day', count_dosequantity=327, count_dosefrequency=1, count_patientuid=230, DM Current -hychqudose='200mg', DM Expected Value='400mg'),
 Row(practiceid=623, dosequantity='200', dosefrequency='take 1 (200MG)  by oral route 2 times every day', count_dosequantity=339, count_dosefrequency=1, count_patientuid=180, DM Current -hychqudose='200mg', DM Expected Value='400mg')]
'''