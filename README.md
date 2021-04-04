# chemical_structure_latex_to_image
creating the image from the latex for chemical strucutures


modules used  in code
shutil,
os,
pdflatex,
pdf2image,
PIL,
save_images-- function will take list of images_names,pdfpath,images_destination_path as arguments
              it will convert the pdf to images and then it will crop the structures from the images and 
              it will save the image with the name specified in the images_names list according to the number
              of image  with respect to index of the name in the list.
crop-- function will take the image path as argument and it will crop chemical structure part of the image.

create_image_from_latex-- function will take the image name and latex as arguments and produce the output image by
            creating the folder "images_from_latex".
reate_images_from_text_file_with_latexes-- function will take path of text file which contains latexes and produce the 
            resulting images in the "images_from_latex" folder and name each images according to the line number in the 
            text file
            
           
           
