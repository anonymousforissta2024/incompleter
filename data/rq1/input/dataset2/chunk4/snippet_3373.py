#Source: https://stackoverflow.com/questions/74600131/pytesseract-pytesseract-has-no-attribute-pytesseract-attribute-error
from passporteye import read_mrz
from pytesseract import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\*<username>*\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

# Process image
mrz = read_mrz("C:\\Users\\*<username>*\\Documents\\UiPath\\imageExtract\\Data\\image1.jpeg")


# Obtain image
mrz_data = mrz.to_dict()

# Printing extracted data
print('Nationality :'+ mrz_data['nationality'])
print('Given Name :'+ mrz_data['names'])
print('Surname :'+ mrz_data['surname'])
print('Passport type :'+ mrz_data['type'])
print('Date of birth :'+ mrz_data['date_of_birth'])
print('ID Number :'+ mrz_data['personal_number'])
print('Gender :'+mrz_data['sex'])
print('Expiration date :'+ mrz_data['expiration_date'])