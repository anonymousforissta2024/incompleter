#Source: https://stackoverflow.com/questions/45911113/formatting-strings-s-returns-typeerror-a-float-is-required
import datetime

date = (datetime.datetime.today().date() - datetime.timedelta(days=100)).strftime("%m/%d/%Y")
date = str(date)
date = date.replace("/","%2F")

def genUrl(account, date, lastName, firstName):
    url = "https://arpmp-ph.hidinc.com/arappl/bdarpdmq/pmqadhocrpt.html?a=&page=recipqry&disp-bdate=%s&disp-edate=%s&recip-list=02685245&output=web&dt-sort-by=rcpdt&mode=Recipient_Query&w_method=POST&suplist=BM0650386&base-prsb=0&base-phrm=0&base-recip=1&tot-recip=1&report=PHY&recip-sex=A&recip-dob=01%2F21%2F1964&account-id=%s&date=%s&dob-days=0&recip-name=%s&recip-fname=%s&enum-read-cnt=2&enum-keep-cnt=1&etime=5&pagename=pmqrecipqry&pdmdir=arpdm&pdmstate=ar&scriptname=%2Farappl%2Fbdarpdmq&exprecip=yes" %(date, str(datetime.datetime.now()), account, date, lastName, firstName)
    print(url)

genUrl("example",date, "Smith", "Jogn")