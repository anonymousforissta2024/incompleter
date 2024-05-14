#Source: https://stackoverflow.com/questions/76009794/why-when-i-run-this-code-return-attributeerror-nonetype-object-has-no-attrib
import pandas as pd
import numpy as np
import sys
import os
path = r'C:/Users/' +  os.getlogin()  +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos'
sys.path.insert(0, path)
import PyPDF2
import tabula
import re
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pdfplumber
#import EjecutarQuery as EQ 
#from datetime import datetime
#from datetime import timedelta
#import ToolsBI

#%%
#Leemos archivo excel de Base
path = r'C:/Users/'+  os.getlogin()  +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos/Confimación y Facturación Apple/Base proveedor/Base-prueba.xlsx'
detalle_base = pd.read_excel(path, sheet_name="Base")
detalle_base = detalle_base.reindex(columns = ['Factura', 'New OC', 'PRODUCTO', 'NOMBRE', 'Units', 'CAJAS', 'SKU Falabella', 'Costo Unitario', 'Monto total', 'Diferencia Informada', 'Comentarios'])

def extract_pdf_data(file_names):
    all_data = []
    for file_name in file_names:
        with pdfplumber.open(file_name) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()
            numero_factura = re.search(r'N°\s*(d\+)', text).group(1)
            cantidad = re.search(r'Cant.\s*(d\+)', text).group(1)
            costo_unitario_fact = re.search(r'Valor unitario\s*(d\+)', text).group(1)
            valor_total_fact = re.search(r'Valor\s*(d\+)', text).group(1)
            data = [numero_factura, cantidad, costo_unitario_fact, valor_total_fact]
            all_data.append(data)
    return all_data

def convert_pdfs_to_excel(directory, excel_file_name, excel_path):
    file_names = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.pdf')]
    all_data = extract_pdf_data(file_names)
    flat_data = [item for sublist in all_data for item in sublist]
    df = pd.DataFrame(flat_data, columns=['Numero Factura', 'Cantidad', 'Costo Unitario', 'Valor Total'])
    df.to_excel(excel_file_name, index=False)
    
convert_pdfs_to_excel(r'C:/Users/'+ os.getlogin() +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos/Confimación y Facturación Apple/Facturas Apple', 'datos.xlsx', 'C:/Users/'+ os.getlogin() +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos/Confimación y Facturación Apple')