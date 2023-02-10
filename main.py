import PyPDF2
from PyPDF2 import PdfReader

# Open the PDF file
pdf_file = open('HRPolicy_USAID.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)


# Extract the metadata
pdf_info = pdf_reader.metadata

# Extract the file name and section from the metadata
file_name = pdf_info.get(b'/Title', 'Unknown')
section = pdf_info.get(b'/Section', 'Unknown')

# Close the PDF file
pdf_file.close()

# Print the extracted data
print('File name:', file_name)
print('Sections name:', section)
print('PDF File:', pdf_reader)

reader = PdfReader("HRPolicy_USAID.pdf")

keyword = "salary"

i = 0
number_of_pages = len(reader.pages)

pages_with_keyword = []


for i in range(len(reader.pages)):
    page = reader.pages[i]


    page_text = page.extract_text()

    if "salary" in page_text:
        pages_with_keyword.append(i+1)
    

print("HR Policy pages [page numbers] that mention the keyword: ")

for i in range(len(pages_with_keyword)):
    print(str(pages_with_keyword[i]) + "\n")


