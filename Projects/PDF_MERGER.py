from PyPDF2 import PdfWriter

merge = PdfWriter()
pdfs =[]
n = int(input("😁😁YOO! How many pdfs you are going to merger?\n"))

for i in range (0, n):
  name = input(f"Enter the name of PDFs  {i+1}-> ")
  pdfs.append(name)

for pdf in pdfs:
  merge.append(pdf)  

merge.write("merged-pdf.pdf") 
merge.close() 