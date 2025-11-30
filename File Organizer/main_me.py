import os
import shutil


try:
    scraping_path="C:\\Users\\PC\\Downloads"
    # destined_loct="C:\\Users\\PC\\Desktop"

    destined_path=os.path.join("C:\\Users\\PC\\Desktop","Pdfs")
    # destined_path=os.path.join(os.path.expanduser('~'), "Desktop", "All PDFs") Other way of doing it

    if not os.path.exists(destined_path):
        os.mkdir(destined_path)
        print("The folder is created")
    # else:
    #     print("File already exists")


    for file in os.listdir(scraping_path):
        if file.endswith(".pdf"):
            source_file=os.path.join(scraping_path,file)
            shutil.move(source_file,destined_path)
            print(f"File moved :-{file}")
            
except FileExistsError:
    print("The folder already exists")

except FileNotFoundError:
    print("The source folder does not exist")

