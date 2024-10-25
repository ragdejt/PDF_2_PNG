# Import necessary libraries.
import os
import time
import fitz
from pathlib import Path
from rich import print
from tqdm import tqdm
from utils.troubleshooting import DATE_TIME
from utils.ascii_text import *
# Path's 
user_path = Path.home()
script_path = user_path / ("PDF_2_PNG")
png_folder = script_path / ("PNG")
pdf_folder = script_path / ("PDF")
# Create directory                                                                                 
def create_directory():
    script_path.mkdir(exist_ok=True)
    png_folder.mkdir(exist_ok=True)
    pdf_folder.mkdir(exist_ok=True)
# Date / Time.                                                                                     
def date_time():
    print(time.strftime(DATE_TIME).center(100, "-"))
    input("[Press ENTER to continue]".center(100, "-"))
# List PDF folder.                                                                                 
def list_pdf_folder():
    print(PDF_FOLDER)
    for i, dir in enumerate(os.listdir(pdf_folder), start=1):
        print(f"[{i}]:", f"[green]{dir}[/]")
    date_time()
# List PNG folder.                                                                                 
def list_png_folder():
    print(PNG_FOLDER)
    for i, dir in enumerate(os.listdir(png_folder), start=1):
        print(f"[{i}]:", f"[green]{dir}[/]")
    date_time()
# PDF_2_PNG.                                                                                       
def pdf_2_png():
    try:
        print(PDF_2_PNG)
        pdf_name = str(input("[Enter the name of the PDF you want to convert]:"))
        pdf_path = pdf_folder / (pdf_name + ".pdf")
        png_path = png_folder / (pdf_name)
        if os.path.exists(pdf_path):
            png_path.mkdir()
            file = fitz.open(pdf_path) 
            for page_num in tqdm(range(file.page_count)):
                page = file[page_num]
                image = page.get_pixmap()
                image_path = os.path.join(png_path , f"Pagina_{page_num + 1}.png")
                image.save(image_path)
            print(
                "[green][Conversion Completed][/]\n"
                f"[Pages]: {file.page_count}"
            )
        else:
            print("[Error]: File not found")
    except FileExistsError:
        raise FileExistsError
# Menu.                                                                                            
def menu():
    while True:
        try:
            print(MENU)
            menu_input = int(input("[Your answer]: "))
            match menu_input:
                case 0:
                    exit()
                case 1:
                    list_pdf_folder()
                case 2:
                    list_png_folder()
                case 3:
                    pdf_2_png()
                case _:
                    raise ValueError
        except ValueError:
            raise ValueError