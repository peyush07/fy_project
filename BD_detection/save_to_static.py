import json
import cv2
import matplotlib.image as im
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from PIL import ImagePath
import imageio as im
import os

def save_to_static(path1, path2, img3):
    if("santa-rosa-wildfire" in path1):
        img1 = Image.open(path1).convert('RGBA')
        img2 = Image.open(path2).convert('RGBA')
        head1, tail1 = os.path.split(path1)
        head2, tail2 = os.path.split(path2)

        existing_files = sorted(os.listdir("/home/peyush/myproject/static/srwf/pre"))
        if tail1 not in existing_files:        
            im.imwrite("/home/peyush/myproject/static/srwf/pre/"+tail1 , img1)
            im.imwrite("/home/peyush/myproject/static/srwf/post/"+tail2 , img2)
            im.imwrite("/home/peyush/myproject/static/srwf/output/"+tail2, img3)

    if("guatemala-volcano" in path1):
        img1 = Image.open(path1).convert('RGBA')
        img2 = Image.open(path2).convert('RGBA')
        head1, tail1 = os.path.split(path1)
        head2, tail2 = os.path.split(path2)

        existing_files = sorted(os.listdir("/home/peyush/myproject/static/gvol/pre"))
        if tail1 not in existing_files:        
            im.imwrite("/home/peyush/myproject/static/gvol/pre/"+tail1 , img1)
            im.imwrite("/home/peyush/myproject/static/gvol/post/"+tail2 , img2)
            im.imwrite("/home/peyush/myproject/static/gvol/output/"+tail2, img3)


    if("hurricane-harvey" in path1):
        img1 = Image.open(path1).convert('RGBA')
        img2 = Image.open(path2).convert('RGBA')
        head1, tail1 = os.path.split(path1)
        head2, tail2 = os.path.split(path2)

        existing_files = sorted(os.listdir("/home/peyush/myproject/static/harvey/pre"))
        if tail1 not in existing_files:        
            im.imwrite("/home/peyush/myproject/static/harvey/pre/"+tail1 , img1)
            im.imwrite("/home/peyush/myproject/static/harvey/post/"+tail2 , img2)
            im.imwrite("/home/peyush/myproject/static/harvey/output/"+tail2, img3)

    if("palu-tsunami" in path1):
        img1 = Image.open(path1).convert('RGBA')
        img2 = Image.open(path2).convert('RGBA')
        head1, tail1 = os.path.split(path1)
        head2, tail2 = os.path.split(path2)

        existing_files = sorted(os.listdir("/home/peyush/myproject/static/ptsu/pre"))
        if tail1 not in existing_files:        
            im.imwrite("/home/peyush/myproject/static/ptsu/pre/"+tail1 , img1)
            im.imwrite("/home/peyush/myproject/static/ptsu/post/"+tail2 , img2)
            im.imwrite("/home/peyush/myproject/static/ptsu/output/"+tail2, img3)
