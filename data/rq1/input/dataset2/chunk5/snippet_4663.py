#Source: https://stackoverflow.com/questions/65887955/i-am-having-a-nonetype-error-on-exiting-gui
import os 
import shutil
import sys
import math
import openpyxl
from datetime import datetime
from docx import Document
from docx.shared import Inches
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
import PySimpleGUI as sg
import traceback

# Define the window's contents

tab1_layout =  [
          [sg.Text('Copy/Paste the row of the SC, CA, or CC from Teams')],
          [sg.Text('Customer name should have - rather than spaces')],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,5), key='-OUTPUT-')],
          [sg.Checkbox('Delete Revision History', default=True, key='-Rev-'), sg.Checkbox('My second Checkbox!')],
         
          
          ]   

tab2_layout = [[sg.T('Use this page to:')],   
               [sg.T('    -Create a CC from a CA')], 
               [sg.T('    -Remove header info from a SOW to give to another SOW')], 
               [sg.T('    -Copy tables from one SOW to another')], 
               [sg.Radio('CA to CC', "RADIO", default=True, key='-CAtoCC-', enable_events=True), sg.Radio('Remove Customer Info', "RADIO", key='-RemoveCust-', enable_events=True), sg.Radio('Copy Tables', "RADIO", key='-Tables-', enable_events=True)],
               [sg.In(key='in1')],
               [sg.In(key='in2')],
               [sg.Checkbox('Header',disabled = True, key='-Head-'),sg.Checkbox('Hardware',disabled = True, key='-Hard-'),sg.Checkbox('Software', disabled = True, key='-Soft-'),sg.Checkbox('Calibration', disabled = True, key='-Cal-'),sg.Checkbox('Deliverables', disabled = True, key='-Deli-')],

               
               ]    

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, key='Tab 1'), sg.Tab('Tab 2', tab2_layout, key='Tab 2')]], key='tab')],   
          [sg.Button('Create'), sg.Button('Clear'), sg.Button('Quit')]
          ]   

tableNames = ['Header', 'Hardware', 'Software', 'Calibration', 'Deliverables']
tableKeys = ['-Head-', '-Hard-', '-Soft-', '-Cal-', '-Deli-']

# Create the window
window = sg.Window('SOW and CA Creator', layout)
 
try:
   
    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()      
        
        
        if values['-Tables-'] == True:
            for i in tableKeys  :
               window[i].Update(disabled = False)
               continue

        if values['-Tables-'] == False:
            for i in tableKeys  :
                window[i].Update(disabled = True)
                continue

        if event == 'Create' and values['-in1-'] != '' and values['-in2-'] != '' and values['tab'] == 'Tab 2' and values['CAtoCC']:
            pass


       # See if user wants to quit or window was closed
        if event in (sg.WINDOW_CLOSED, 'Quit' ):
            window.close()
            break
        


except Exception as e:
    window.close()
    tb = traceback.format_exc()
    sg.Print(f'An error happened.  Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)