import PyPDF2, glob

def pdf_txt(direct):
    for file_name in direct:
        print(file_name.split(".")[0])
        with open(file_name, 'rb') as infile:
            pdfreader = PyPDF2.PdfReader(infile)
            pageobj = pdfreader.pages[0]
            text = pageobj.extract_text()

            file1=open(str(file_name.split(".")[0])+".txt", "a")
            file1.writelines(text)
    print("PDF to TXT conversion complete.")

directory = glob.glob('C:/your/ptch/to/folder/*.pdf')
pdf_txt(directory)