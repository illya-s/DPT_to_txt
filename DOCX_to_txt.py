import glob, docx2txt

def docx_txt(direct):
    for file_name in direct:
        with open(file_name, 'rb') as infile:
            with open(file_name[:-5]+'.txt', 'w', encoding='utf-8') as outfile:
                doc = docx2txt.process(infile)
                outfile.write(doc)
    print("DOCX to TXT conversion complete.")

directory = glob.glob('C:/Users/Ilya/Desktop/songs/*.docx')
docx_txt(directory)