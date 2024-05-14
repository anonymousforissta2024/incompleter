#Source: https://stackoverflow.com/questions/44129593/typeerror-the-first-argument-must-be-callable
import schedule  
import time  

def rank():  
    import new_user as nu  
    nu.new_user()  
    print('successfully loaded')  
    return  

schedule.every(5).minutes.do(rank())  

while 1:  
    schedule.run_pending()  
    time.sleep(1)  