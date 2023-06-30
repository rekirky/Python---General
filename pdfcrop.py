import PyPDF2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename()

def crop_pdf(input_file, output_file, crop_box):
    # Open the input PDF file
    pdf_reader = PyPDF2.PdfReader(input_file)
    
    # Create a PDF writer object to write the output file
    pdf_writer = PyPDF2.PdfWriter()
    
    # Loop through each page of the input PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Set the crop box of the page
        page.mediabox = crop_box
        
        # Add the cropped page to the output PDF
        pdf_writer.addPage(page)
    
    # Write the output PDF to a file
    with open(output_file, 'wb') as f:
        pdf_writer.write(f)

# Example usage
input_file = filename
output_file = 'output.pdf'
crop_box = (0, 0, 200, 200)
crop_pdf(input_file, output_file, crop_box)