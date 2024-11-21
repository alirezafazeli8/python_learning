from PyPDF2 import PdfReader, PdfWriter

# read marker page
reader_marker = PdfReader("../assets/wtr.pdf").pages[0]
# read target pdf
pdf_reader = PdfReader("../assets/twopage.pdf")
# create new pdf obj
writer = PdfWriter()

# loop over target pdf pages
for page in pdf_reader.pages:
    # merge target pdf pages with marker page
    page.merge_page(reader_marker)
    # add new page to new pdf
    writer.add_page(page)

# save pdf to new path
writer.write("../assets/marker_new.pdf")
