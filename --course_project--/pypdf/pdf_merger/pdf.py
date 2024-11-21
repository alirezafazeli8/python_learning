import sys
from PyPDF2 import PdfMerger

try:
    # read terminal args
    pdf_lists = sys.argv[1:]

    # create pdf merger object
    pdf_merger = PdfMerger()

    # add pdf's to pdf merger
    for pdf in pdf_lists:
        pdf_merger.append(pdf)

    # create new pdf
    pdf_merger.write("../assets/super_pdf.pdf")
    pdf_merger.close()
    print("Done ! file saved in your computer")

except IndexError:
    print("Pleas type to pdf's file path")
# handle file path error
except FileNotFoundError:
    print("I cant find pdf file .")
