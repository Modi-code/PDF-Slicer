import os
import tkinter as tk
from tkinter import filedialog
from pypdf import PdfReader, PdfWriter

root = tk.Tk()
root.withdraw()

# Open the file dialog to select input pdf
file_path = filedialog.askopenfilename(
    title="Select a File",
    filetypes=[("Text Files", "*.pdf")]
)

# Open folder dialog to select output location
dest_pdf_dir = filedialog.askdirectory(
    title="Select a Directory"
)

if file_path == "" or dest_pdf_dir == "":
    print("Error: Both a directory and a file have to be selected")
    exit(0)

# Set the starting page number
counter = 1

if not os.path.exists(dest_pdf_dir):
    os.makedirs(dest_pdf_dir)

reader= PdfReader(file_path)

for i,page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    output_filename=f"{i+counter}.pdf"
    output_path=os.path.join(dest_pdf_dir,output_filename)
    with open(output_path,"wb") as output_pdf:
          writer.write(output_pdf)
print(f'Successfully split {file_path} into {len(reader.pages)} pages')