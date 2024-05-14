#Source: https://stackoverflow.com/questions/54028479/typeerror-printboardpg-object-does-not-support-indexing
import csv
import re
import datetime
from task import Task
from task_list import TaskList


class Worklog():
    def __init__(self):
        self.filename = "work_log.csv"
        self.tasklist = TaskList()
        self.tasklist.read_task_from_file(self.filename)

    def search_by_date(self):
        for d, i in enumerate(self.tasklist.dates()):
            print(d+1, ':', i)
        # while True:
        #     datereq = input("Select Number To See Tasks For A Date").strip().lower()
        #     try:
        #         datereq = int(datereq)
        #         return datereq
        #     except ValueError:
        #         print("Invalid Entry. Please try again")
        #         continue

    def search_by_time(self):
        pass

    def exact_search(self):
        pass

    def pattern_search(self):
        pass

    def add_task(self):
        task = Task()
        task.input_task()
        task.input_minutes()
        task.input_notes()
        task.date = datetime.date.today()
        self.tasklist.app_task(task)
        self.tasklist.save_task_to_file(self.filename,task)

    def lookup_task(self):
        if len(self.tasklist.task_list) == 0:
            print("Your task log is empty.\n")
            input("Hit Enter to add a new task.")
        else:
            while True:
                lookup = input("Lookup by Date(D), Time(T), Exact Search(E) or Pattern(P): ")
                lookup.lower()

                if lookup == 'd':
                    self.search_by_date()
                    break
                elif lookup == 't':
                    self.search_by_time()
                    break
                elif lookup == 'e':
                    self.exact_search()
                    break
                elif lookup == 'p':
                    self.pattern_search()
                    break
                else:
                    print("Sorry invalid option. Please try again")

    def start_message(self):
        while True:

            q = input("Add New Task(1) or Lookup Task(2) or Quit(3): ".strip().lower())

            if q == "1":
                self.add_task()

            elif q == "2":
                self.lookup_task()

            elif q == "3":
                exit()

            else:
                print("Sorry that's an invalid entry. Please try again.")
                continue

if __name__ == '__main__':
    log = Worklog()
    log.start_message()