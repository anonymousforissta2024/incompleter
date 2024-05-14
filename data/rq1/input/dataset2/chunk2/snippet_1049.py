#Source: https://stackoverflow.com/questions/50384627/threading-typeerror-module-object-is-not-callable
import schedule
import time
import psycopg2
import threading
import activity_url_collector
import storage_data_collector

def main():


    def run_threaded(job_func):
        job_thread = threading.Thread(target=job_func)
        job_thread.start()

    schedule.every(3).minutes.do(run_threaded, activity_url_collector)
    schedule.every(3).minutes.do(run_threaded, storage_data_collector)

    schedule.run_all()

    print('Post-Processing-Application is running')

    while True:
            schedule.run_pending()
            time.sleep(1)    

if __name__=="__main__":
    main()