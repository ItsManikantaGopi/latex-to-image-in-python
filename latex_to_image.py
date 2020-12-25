import shutil
import os
from pdflatex import PDFLaTeX
from pdf2image import convert_from_path
from PIL import Image

def crop(file):
    img = Image.open(file)
    area = (300,300, 800, 800)
    cropped_img = img.crop(area)
    cropped_img.save(file)

def save_images(images_names,pdf_path,images_path=""):
# Store Pdf with convert_from_path function
    images = convert_from_path(pdf_path)
    if len(images_names)==0:
        print("names is empty")
        return
    i=0
    for img in images:
        img.save(images_path+"/"+images_names[i]+".jpg", 'JPEG')
        crop(images_path+"/"+images_names[i]+".jpg")
        i+=1
    print("Successfully converted")

def create_image_from_latex(image_name,latex):
    if "rough" not in os.listdir():
        os.mkdir("rough")
    if "images_from_latex" not in os.listdir():
        os.mkdir("images_from_latex")
    f=open("rough/a.tex","w+")
    f.write("\\documentclass{article}\n\\usepackage{chemfig}\n\\begin{document}\n")
    f.write(latex+"\n")
    f.write(r"\end{document}")
    f.close()
    #print(os.getcwd()+"/a.tex")
    #tex="/a.tex"
    pdfl = PDFLaTeX.from_texfile('rough/a.tex')
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
    f=open("rough/a.pdf","wb")
    f.write(pdf)
    f.close()
    save_images([image_name],"a.pdf","images_from_latex")
    os.remove("rough/a.pdf")
    shutil.rmtree("rough")
#create_image_from_latex("new_image",lat)
def create_images_from_text_file_with_latexes(text_file):
    with open(text_file) as f:
        latexes=f.readlines()
        ind=1
        for lat in latexes:
            create_image_from_latex("%0.3d_"%ind,lat)
            ind+=1
