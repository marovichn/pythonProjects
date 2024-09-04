import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")
    merger.close()


pdf_combiner(inputs)

# Open the merged PDF and the watermark PDF
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# Merge the watermark with each page of the template PDF
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))  # Adjusted function name to lowercase merge_page
    output.addPage(page)

# Save the watermarked PDF to a new file
with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)