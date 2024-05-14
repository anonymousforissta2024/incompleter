#Source: https://stackoverflow.com/questions/43679070/typeerror-not-all-arguments-converted-during-string-formatting-during-uploadi
import pymysql as psl
con6s = psl.connect(host='myhost',database='mydatabase',user='usr',passwd='12345')
c6s = con6s.cursor()
c6s.execute( "INSERT INTO %s (stmp,dat,tm,tc,mc,sd,rp,st,stf,stt) VALUES(?,?,?,?,?,?,?,?,?,?)" % (str(db)), (stmp,dat,tm,tc,mc,sd,rp,st,stf,stt))
con6s.commit()
con6s.close()