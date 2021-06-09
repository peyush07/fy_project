import json
import cv2
import matplotlib.image as im
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from PIL import ImagePath
import imageio as im


def draw_pol(imagepath2):
    f = open('/tmp/inference/inference.json')
    # x = bool("santa_rosa_wildfire" in imagepath2)
    # if(x)
    # f = open('/home/peyush/fy_project/xView2/output/inference/inference_gv_23.json')
    data = json.load(f)
    
    
    # data = json.load(f)
    # print(data['features']['xy'])
    x = data['features']['xy']
    # print(x)
    damage_type = []
    for i in x:
        damage_type.append((i['properties']['subtype']))
    # for i in damage_type:
    #     print(i)
    temp = []
    for i in x:
        temp.append(i['wkt'])
    # print(temp)
    test = temp[0]
    # print(test)
    for i in range(len(temp)):
        temp[i] = temp[i].replace("POLYGON ((","") 
        temp[i] = temp[i].replace("))","")
    # print(temp)
    res = []    # a list that stores a list of polygon coordinates
    for i in temp:
        res.append(i.split(','))
    # print(res)

    t = []                               #stores each tuple as list for converting to float
    coordinates = []                     # coordinates of th polygons in required format
    temp2 = []                           #temporary list for formatting each element of list with the res list
    for i in range(len(res)):
        for j in res[i]:
            t = j.split(' ')
            t[0] = float(t[0])
            t[1] = float(t[1])
            temp2.append(tuple(map(int,t)))
        coordinates.append(temp2)
        temp2 = []
    # print(coordinates)
    img = Image.open(imagepath2).convert('RGBA')
    # img.show()
    img2 = img.copy()

    for i in range(len(damage_type)):
        if damage_type[i] == "no-damage":
            color = "green"
        if damage_type[i] == "minor-damage":
            color = "blue"
        if damage_type[i] == "major-damage":
            color = "yellow"
        if damage_type[i] == "destroyed":
            color = "red"
        draw = ImageDraw.Draw(img2)
        draw.polygon(coordinates[i], fill=color)
        img3 = Image.blend(img, img2, 0.5)
    
    #img3.show()
    im.imwrite("/var/www/html/output/output_polygons.png", img3)
    return img3