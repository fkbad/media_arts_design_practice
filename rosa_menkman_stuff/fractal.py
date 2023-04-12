# import sys
import glob
from typing import Tuple, List#, Dict, Union, Optional, Set
# import random
import numpy as np
#import imageio
from PIL import Image
import math

# global parameters
global_image = Image.open("mandelbrot.png")
output_path = "output/"
temp = output_path + "temp"
WIDTH, HEIGHT = global_image.size
ROTATION_BOUND = 45

def get_copy():
    """
    return copy of the original image
    """
    return global_image.copy()

def mycrop(coordinate: Tuple[int,int], dimension_tuple: Tuple[int,int]):
    image = get_copy()
    width, height = dimension_tuple
    (left, upper) = coordinate
    (right, lower) = (left + width, upper + height)
    return_image = global_image.crop((left, upper, right, lower))
    return return_image

def get_Nth_coordinates(n: int):
    """
        meant to take the img global variable and output N images, each being [(x/4 * width) by (x/4 * height) for x from 3-1]

        input: n: the scale. eg 4 means split into 4ths
        outputs list of images
    """
    x_coords = np.linspace(0,WIDTH,n,endpoint=False,dtype=int)
    y_coords = np.linspace(0,HEIGHT,n,endpoint=False,dtype=int)
    # list of tuples scaled to the 4th
    coords = np.rec.fromarrays([x_coords,y_coords]).tolist()
    return coords

def get_width_and_height_to_crop_from_tuple(tuple: Tuple[int,int]):
    """
        to get inputs to feed into
    """
    x,y = tuple
    return (WIDTH-x,HEIGHT-y)

def crop_into_Nths(n=4):
    """
        meant to take the img global variable and output N images, each being [(x/4 * width) by (x/4 * height) for x from 3-1]

        outputs list of images
    """
    coords = get_Nth_coordinates(n)
    # print(coords)
    # empty list to store my N images
    image_list = []
    for coordinate in coords:
        dimension_tuple = get_width_and_height_to_crop_from_tuple(coordinate)
        # print(f"coord: {coordinate}")
        # print(f"dimension: {dimension_tuple}")
        cropped_image = mycrop(coordinate,dimension_tuple)
        image_list.append(cropped_image)
        # cropped_image.show()

    return image_list

def new_temp_jpg_name(label: int,i_am_a_png=False):
    if i_am_a_png:
        return temp + str(label) + ".png"
    return temp + str(label) + ".jpg"

def to_jpeg(image,label: int, quality=0):
    # https://stackoverflow.com/questions/43258461/convert-png-to-jpeg-using-pillow
    rgb_img = image.convert('RGB')

    if quality == 96:
        rgb_img.save(new_temp_jpg_name(label,i_am_a_png=True), quality=0)

    else:
        rgb_img.save(new_temp_jpg_name(label), quality=0)
    
def get_N_quality_numbers(n: int):
    # the 96 is because jpeg quality is at most 95, so this is used to not convert the final image
    return np.linspace(0,96,n,endpoint=True,dtype=int).tolist()

def jpegify_list(image_list):
    qualities = get_N_quality_numbers(len(image_list))
    for label,image in enumerate(image_list):
        # print(qualities[label])
        to_jpeg(image,label,qualities[label])

    image_filenames = glob.glob("output/temp*")
    image_filenames.sort()

    image_list = []
    for image_filename in image_filenames:
        file = open(image_filename, 'rb')
        img = Image.open(file)
        print("iterating")
        image_list.append(img)

    # https://stackoverflow.com/questions/5324647/how-to-merge-a-transparent-png-image-with-another-image-using-pil
    background = image_list.pop(0)
    print(f"length of list = {len(image_list)}")
    rotations = np.linspace(0,ROTATION_BOUND,len(image_list),endpoint=True,dtype=int)
    print(rotations)
    for index,un_rotated_image in enumerate(image_list):
        width, height = un_rotated_image.size
        # print(rotations[index])
        image = un_rotated_image.convert("RGBA").rotate(-1*rotations[index])
        
        def modify_paste_coord(dimension_tuple: Tuple[int,int]):
            width,height = dimension_tuple

            width_mod = 1.5
            height_mod = 1.1

            width *= width_mod
            height *= height_mod

            output_width = WIDTH - width
            output_height = HEIGHT - height
            # print(output_width,output_height)
            return (int(output_width),int(output_height))
            
        background.paste(image,modify_paste_coord((width,height)),image.convert("RGBA"))

    background.show()
    background.save("final1.png")


list = crop_into_Nths(45)
jpegify_list(list)
