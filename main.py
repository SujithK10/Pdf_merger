import PyPDF2

# List of PDF files to merge
pdf_files = ['North India.pdf', 'South India.pdf']

# Create a PDF merger object
merger = PyPDF2.PdfMerger()

# Loop through all PDF files and append them to the merger object
for pdf in pdf_files:
    merger.append(pdf)

# Write out the merged PDF to a file
with open('merged_document.pdf', 'wb') as output_pdf:
    merger.write(output_pdf)

print("PDFs merged successfully!")
