from pdf2image import convert_from_path, convert_from_bytes
import os
from PIL import Image

cwd = os.getcwd()
input_path = cwd +"/PDF/"
destination_path = cwd +"/PPM/"
image_save_path = cwd +"/PPM 2 JPG/"


def conversion(input_files):
    # conversion method
    try:
        for x in input_files:
            dest_file = input_path + x
            dest_path = destination_path + x + '/'
            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)
            images_from_path = convert_from_path(dest_file, output_folder=dest_path)

        for x in input_files:
            dest_path = destination_path + x + '/'
            txt_files = [f for f in os.listdir(dest_path) if f.endswith('.ppm')]
            # print(txt_files)
            counter = 0
            for txt_file in txt_files:
                image = Image.open(dest_path + txt_file)
                image_input_path = image_save_path + x + '/'
                if not os.path.isdir(image_input_path):
                    os.makedirs(image_input_path)
                image.save(image_input_path + str(counter) + ".jpg")
                counter += 1
    except:
        return "Exception Occured"

    else:
        return "conversion successfull"









input_files = [f for f in os.listdir(input_path) if f.endswith('.pdf')]


if len(input_files)>0:
    print(conversion(input_files))
else:
    print("There are no input PDF files. Please paste some files in PDF Folder")

    








