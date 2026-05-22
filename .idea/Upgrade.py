from pypdf import PdfReader, PdfWriter
import os,time,re

#only change dest and make sure numbering files from 1
dest="Nmap"


count=1
ads=2
input_pdf = f"C:/Users/Flex/Desktop/{count}.pdf"
while os.path.exists(input_pdf):
    reader= PdfReader(input_pdf)
    for i,page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename=f"{i+ads}.pdf"

        output_path=os.path.join(f"C:/Users/Flex/Desktop/{dest}",output_filename)
        with open(output_path,"wb") as output_pdf:
            writer.write(output_pdf)
            print(f'created {i+ads}')
    ads+=len(reader.pages);
    count+=1;
    input_pdf = f"C:/Users/Flex/Desktop/{count}.pdf"
