#Source: https://stackoverflow.com/questions/74322469/python3-multiprocessing-pool-in-pyqt5-qthread-raises-typeerror-cannot-pickle-ta
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal , pyqtSlot

import time

import os

import multiprocessing as mp


def work(x):
    # print('os.getpid() : {}'.format(os.getpid()), time.time(),'\n')
    time.sleep(1)
    print(x)
    
    return x
     

class TaskThread(QThread):
    
    results = pyqtSignal(object)
    
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        
        print("Thread app:", int(QThread.currentThread().currentThreadId()))
    
    
    @pyqtSlot()
    def run(self):
        
        print('run..................')
        
        print("Thread app run :", int(QThread.currentThread().currentThreadId())) ## i.e. 140079831918336
        
        print("Thread app run :", (QThread.currentThread())) ## i.e. <__main__.TaskThread object at 0x7f66ed6f9280>
        
        print("Thread app run :", (QThread.currentThread().currentThreadId())) ## i.e. <sip.voidptr object at 0x7f66eceb94b0>
        
        testFL = [1, 2, 3, 4, 5, 6]
        pool = mp.Pool(6)
       
        
       
        result = pool.map(self.work, testFL)  # TypeError: cannot pickle 'TaskThread' object
        
        # result = pool.map(work, testFL)  ## this works using work at top level 
        
        pool.close()
        pool.join()
        
        
        # result = []
        # for i in testFL:
            
        #     result.append(self.work(i))
            
            
        
        
        # print(result)
        # print(type(result))
        
        self.results.emit(result)
        
        print('QThread run finished')
        
    def work(self, x):
        # print('os.getpid() : {}'.format(os.getpid()), time.time())
        # time.sleep(1)
        print(x)
        return x
        
        
class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(100, 100, 300, 50)
        self.setWindowTitle('QThread Demo')
        
        # setup widget
        self.widget = QWidget()
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)       

        self.btn_start = QPushButton('Start', clicked=self.start)

        layout.addWidget(self.btn_start)
        
        print("QMainWindow:", int(QThread.currentThread().currentThreadId()))
        
    def start(self):
        
        self.use_thread()


    def use_thread(self):
        self.thread = TaskThread(self)
        self.thread.finished.connect(self.task_finished)
        
        
        self.thread.results.connect(self.print_qthread_res)
        
        self.thread.start()
    
    @pyqtSlot(object)
    def print_qthread_res(self, objectz):
        
        print('passssed .......... : ', objectz)
        print('type : ', type(objectz))
    
    def task_finished(self):
        
        print('QThread FINISHED !!!!!!!!!')
        pass
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())