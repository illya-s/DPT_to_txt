import os, glob

def rtf_txt(direct):
    files = os.listdir(direct)
    for file in files:
        if os.path.isfile(os.path.join(direct, file)):
            filename, extension = os.path.splitext(file)

        if extension.lower() == ".rtf":
            rtf_file = open(os.path.join(direct, file), "r")
            rtf_content = rtf_file.read()
            rtf_file.close()

            new_name = f"{filename}.txt"
            txt_file = open(os.path.join(direct, new_name), "w")
            txt_file.write(rtf_content)
            txt_file.close()

    print("RTF to TXT conversion complete.")

directory = glob.glob('C:/Users/Ilya/Desktop/songs/*.rtf')
rtf_txt(directory)