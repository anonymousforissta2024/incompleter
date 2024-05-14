#Source: https://stackoverflow.com/questions/72029962/typeerror-rename-src-should-be-string-bytes-or-os-pathlike-not-io-bufferedr
for files in glob.glob(path+"/*.pdf"):
    with open(files, 'rb') as pdf_file:
    
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        page = read_pdf.getPage(0-1)
        text = page.extractText()
        text = " ".join(text.split())

        start = ['from']
        end = ['to']
        text = get_keyword(start, end, text)
        DateList = [text]
        print(text)
        #pdf_file.close()
        
        os.rename(pdf_file,str(i)+".pdf")
    
        tabula.convert_into(str(i)+".pdf", str(i)+".csv", output_format="csv", pages='all')
        
        xlist.append(DateList)
        xlist.append(pd.read_csv(str(i)))
        xmerged = pd.DataFrame()
        i=i+1        