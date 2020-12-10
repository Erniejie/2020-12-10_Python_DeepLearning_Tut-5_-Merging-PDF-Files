# Merging  PDF files

import fitz
file1 = "UKSIPS_Thermal.pdf"
pdf = fitz.open(file1)
num_Pages = pdf.pageCount

pdf2= fitz.open("SBS_U Value Table.pdf")
pdf2.insertPDF(pdf,from_page=0, to_page=num_Pages-1)
pdf2.save("Merged_SBS_UKSIPS.pdf")
