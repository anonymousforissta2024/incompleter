#Source: https://stackoverflow.com/questions/74099141/attributeerror-nonetype-object-has-no-attribute-set-column
import xlwings as xw 
import xlsxwriter as xlsx
import xlrd
import xlwt
from xlutils.copy import copy 
import pandas as pd
import win32com.client as win32
import openpyxl as xl
from openpyxl import load_workbook
import numpy as np 
import datetime
import os.path   
import warnings