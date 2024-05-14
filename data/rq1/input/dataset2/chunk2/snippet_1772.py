#Source: https://stackoverflow.com/questions/37265229/python-filenotfounderror-winerror-3-the-system-cannot-find-the-path-specifie
import shutil
import os
import time

with open('program_started.txt', 'r+') as program_started_file:
    # If program was previously started, runs instructions. If not, continues as normal
    program_started = program_started_file.read()
    if program_started == 'False':
        # Gets src path file and dst path file, write only
        src_file = open('path_src.txt', 'w')
        dst_file = open('path_dst.txt', 'w')
        # Gets src and dst paths
        src_path = input('Enter source path: ') 
        dst_path = input('Enter destination path: ')
        # Writes src and dst paths to txt file
        src_file.write(src_path)
        dst_file.write(dst_path)
        # Moves to beginning of document
        program_started_file.seek(0)
        # Writes 'True' in front of prevous 'False'
        program_started_file.write('True')
        # Removes 'False'
        program_started_file.truncate()
        # Displays 'Completed' message
        print("Completed getting source and destination paths")
    elif program_started == 'True':
        # Gets src path file and dst path file, read only
        src_file = open('path_src.txt', 'r')
        dst_file = open('path_dst.txt', 'r')
        # Checks if flash drive is plugged in
        while True:
            if os.system('cd D:') == 0:
                # Stores src path and dst path in string
                src = src_file.read()
                dst = dst_file.read()
                # If a 2nd backup has been made, removes first and renames 2nd
                if os.path.isdir(dst + "_2") == True:
                    os.rmdir(dst)
                    os.rename(dst + "_2", dst)
                    dst = dst + "_2"
                 # If only a 1st backup was made, creates a 2nd
                elif os.path.isdir(dst) == True:
                    dst = dst + "_2"
                # Copies data
                print('Backing up...', end='')
                shutil.copytree(src, dst)
                print('Completed')
                # Sleeps for 20 minutes
                for x in range(1,12):
                    print("Second: ", x)
                    time.sleep(1)
            else:
                # If no flash drive is detected, tries again in 5 minutes. 
                time.sleep(600)
    else:
        # Error message if program_started.txt != true or false
        print("Error: program_started.txt must only contain either 'True' or 'False'.")