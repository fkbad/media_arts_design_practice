# import sys
from typing import Tuple#, Dict, Union, Optional, Set
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
    print(coords)
    # empty list to store my N images
    image_list = [global_image.copy()]
    for coordinate in coords:
        dimension_tuple = get_width_and_height_to_crop_from_tuple(coordinate)
        print(f"coord: {coordinate}")
        print(f"dimension: {dimension_tuple}")
        cropped_image = mycrop(coordinate,dimension_tuple)
        image_list.append(cropped_image)
        # cropped_image.show()

    return image_list

def new_temp_jpg_name(label: int):
    return temp + str(label) + ".jpg"

def to_jpeg(image,label: int, quality=0):
    # https://stackoverflow.com/questions/43258461/convert-png-to-jpeg-using-pillow
    rgb_img = image.convert('RGB')

    rgb_img.save(new_temp_jpg_name(label), quality=0)
    

list = crop_into_Nths(3)

to_jpeg(list[1],1)
# def jpegify_list(image_list)

