import cv2
import numpy as np
import imageio as im
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from collections import Counter
from PIL import Image
from scipy.misc import imresize, imsave

import io
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from .models import Employee

def find_vector_set(diff_image, new_size):
   
    i = 0
    j = 0
    vector_set = np.zeros((int(new_size[0] * new_size[1] / 25), 25))

    print('\nvector_set shape',vector_set.shape)
    
    while i < vector_set.shape[0]:
        while j < new_size[0]:
            k = 0
            while k < new_size[1]:
                block   = diff_image[j:j+5, k:k+5]
                #print(i,j,k,block.shape)
                feature = block.ravel()
                vector_set[i, :] = feature
                k = k + 5
            j = j + 5
        i = i + 1
        
            
    mean_vec   = np.mean(vector_set, axis = 0)    
    vector_set = vector_set - mean_vec
    
    return vector_set, mean_vec

def find_FVS(EVS, diff_image, mean_vec, new):
    
    i = 2 
    feature_vector_set = []
    
    while i < new[0] - 2:
        j = 2
        while j < new[1] - 2:
            block = diff_image[i-2:i+3, j-2:j+3]
            feature = block.flatten()
            feature_vector_set.append(feature)
            j = j+1
        i = i+1
        
    FVS = np.dot(feature_vector_set, EVS)
    FVS = FVS - mean_vec
    print("\nfeature vector space size",FVS.shape)
    return FVS


def clustering(FVS, components, new):
    
    kmeans = KMeans(components, verbose = 0)
    kmeans.fit(FVS)
    output = kmeans.predict(FVS)
    count  = Counter(output)

    least_index = min(count, key = count.get)            
    print(new[0],new[1])
    change_map  = np.reshape(output,(new[0] - 4, new[1] - 4))
    
    return least_index, change_map


def find_PCAKmeans(imagepath1, imagepath2):
    
    print('Operating')
    
    image1 = im.imread(imagepath1)
    image2 = im.imread(imagepath2)
    print(image1.shape,image2.shape) 
    new_size = np.asarray(image1.shape) / 5
    new_size = new_size.astype(int) * 5
    image1 = imresize(image1, (new_size)).astype(np.int16)
    image2 = imresize(image2, (new_size)).astype(np.int16)
    
    diff_image = abs(image1 - image2)   
    diff_image=diff_image[:,:,1]
    #im.imwrite('./data/diff.jpg', diff_image)
    print('\nBoth images resized to ',new_size)
        
    vector_set, mean_vec = find_vector_set(diff_image, new_size)
    
    pca     = PCA()
    pca.fit(vector_set)
    EVS = pca.components_
        
    FVS     = find_FVS(EVS, diff_image, mean_vec, new_size)
    
    print('\ncomputing k means')
    
    components = 3
    least_index, change_map = clustering(FVS, components, new_size)
    
    change_map[change_map == least_index] = 255
    change_map[change_map != 255] = 0
    
    change_map = change_map.astype(np.uint8)
    kernel     = np.asarray(((0,0,1,0,0),
                             (0,1,1,1,0),
                             (1,1,1,1,1),
                             (0,1,1,1,0),
                             (0,0,1,0,0)), dtype=np.uint8)
    cleanChangeMap = cv2.erode(change_map,kernel)
    #im.imwrite("./data/changemap.jpg", change_map)
    
    im.imwrite("/var/www/html/output/Cleanchangemap.png", cleanChangeMap)
    # img = Image.open("/home/peyush/myproject/media/upload/cleanchangemap.png")
    # img_io = io.BytesIO()
    # img.save(img_io, format = 'png')
    # thumb = InMemoryUploadedFile(img_io, None, '/home/peyush/myproject/media/upload/cleanchangemap.png', 'image/png', img_io(0, os.SEEK_END), None) 
    # ob = Employee()
    # ob.output_image.save(thumb)
    
    # reading the image data from desired directory 
    img = cv2.imread("/var/www/html/output/Cleanchangemap.png") 

    # counting the number of pixels 
    number_of_white_pix = np.sum(img == 255) 
    number_of_black_pix = np.sum(img == 0) 

    # print('Number of white pixels :', number_of_white_pix) 
    # print('Number of black pixels :', number_of_black_pix)
    # percentage = (number_of_white_pix * 100) / (number_of_white_pix + number_of_black_pix)
    # print('Percentage change : ', percentage,'%')
    percentage = (number_of_white_pix * 100) / (number_of_white_pix + number_of_black_pix)
    return percentage