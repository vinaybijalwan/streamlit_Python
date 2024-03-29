##Date:14-02-2023
# import PdfFileWriter and PdfFileReader 
# class from PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader

## create a PdfFileWriter object
out = PdfFileWriter()


##User from 
#pdf_file = input()


# Open our PDF file with the PdfFileReader
file = PdfFileReader("1.pdf")

# Get number of pages in original file
num = file.numPages


# Iterate through every page of the original 
# file and add it to our new file.
for idx in range(num):
    
    # Get the page at index idx
    page = file.getPage(idx)
      
    # Add it to the output file
    out.addPage(page)


##user input paswd 

#pass = input('Enter Password')
# Create a variable password and store 
# our password in it.
password = "pass"


# Encrypt the new file with the entered password
out.encrypt(password)

# Open a new file "myfile_encrypted.pdf"
with open("myfile_encrypted.pdf", "wb") as f:
    
    # Write our encrypted PDF to this file
    out.write(f)