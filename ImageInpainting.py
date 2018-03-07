# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:37:16 2018
OpenCV-Python Tutorials » Computational Photography » Image Inpainting
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:37:16 2018
OpenCV-Python Tutorials » Image Processing in OpenCV » Interactive Foreground Extraction using GrabCut Algorithm
@author: zzx_pc
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

draw = False

img = cv2.imread('E:\python\opencv\lena.jpg')
img_temp = img.copy()
img_real = img.copy()
mask = np.zeros(img.shape[:2],np.uint8)
mask_temp = mask.copy()

def nothing(x):
    pass

def draw_line(event,x,y,flags,param):
    global draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.circle(img_temp, (x,y),t,(255,255,255),-1)
            cv2.circle(mask_temp, (x, y), t, 255, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img_temp, (x, y), t, (255, 255, 255), -1)
        cv2.circle(mask_temp, (x, y), t, 255, -1)
    else:
        pass

def get_tar():
    global t,reset,apply
    reset = cv2.getTrackbarPos(switch,'image')
    apply = cv2.getTrackbarPos(switch1, 'image')
    t = cv2.getTrackbarPos('T','image')

cv2.namedWindow('image')

# create trackbars for thickness
cv2.createTrackbar('T','image',0,20,nothing)

# create switch for ON/OFF functionality
switch = '0 : ok \n1 : reset'
cv2.createTrackbar(switch, 'image',0,1,nothing)

switch1 = '0 : draw \n1 : apply'
cv2.createTrackbar(switch1, 'image',0,1,nothing)

cv2.setMouseCallback('image', draw_line)

while(1):
    cv2.imshow('image',img_temp)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    get_tar()

    if reset == 1:
        img_temp = img.copy()
        img_real = img.copy()
        mask_temp = mask.copy()

    else:
        pass

    if apply == 1:
        cv2.imwrite('E:\python\opencv\lena_mask.jpg',mask_temp)
        newmask = cv2.imread('E:\python\opencv\lena_mask.jpg',0)

        mask_temp[newmask == 0] = 0
        mask_temp[newmask == 255] = 1

        img_real = cv2.inpaint(img, mask_temp, 3, cv2.INPAINT_TELEA)  # cv2.INPAINT_NS采用另一种修复算法
        img_temp = img_real.copy()
    else:
        pass


cv2.destroyAllWindows()