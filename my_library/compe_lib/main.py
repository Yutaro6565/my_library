# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Patch
from PIL import Image, ImageDraw

def make_image_from_pdf(input_folder,output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            pdfname,_=os.path.splitext(filename)
            input_path = os.path.join(input_folder, filename)
            output_directory_path = os.path.join(output_folder, f"{pdfname}")
            
        pdf_file = input_path
    
        if not os.path.exists(output_directory_path):
            os.makedirs(output_directory_path)
    
        # Open the PDF file
        pdf_document = fitz.open(pdf_file)
    
        # Iterate through each page and convert to an image
        for page_number in range(pdf_document.page_count):
            # Get the page
            page = pdf_document[page_number]
    
            # Convert the page to an image
            pix = page.get_pixmap()
    
            # Create a Pillow Image object from the pixmap
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    
            try:
                image.save(f"{output_directory_path}/page_{page_number + 1}.png")
                print(f"Saved: {page_number+1}")
            except Exception as e:
                print(f"Error saving : {e}")
            finally:
                image.close()  # メモリ解放
    
        # Close the PDF file
        pdf_document.close()
