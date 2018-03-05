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
mode = True
ba_fo = False
x0,y0,x1,y1 = -1,-1,-1,-1

img = cv2.imread('E:\python\opencv\\roi.jpg')
img_temp = img.copy()
img_real = img.copy()
mask = np.zeros(img.shape[:2],np.uint8)
mask_temp = np.full(img.shape[:2],128,np.uint8)
mask_real = mask.copy()

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

def nothing(x):
    pass

#前景mask是1，背景mask是0
def draw_label(event,x,y,flags,param):
    global draw,mode,x0,y0,x1,y1,switch,t
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        x0,y0 = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            if mode != True:
                if ba_fo == False:
                    cv2.circle(img_temp, (x,y),t,(0,0,0),-1)
                    cv2.circle(mask_temp, (x, y), t, 0, -1)
                else:
                    cv2.circle(img_temp, (x,y),t,(255,255,255),-1)
                    cv2.circle(mask_temp, (x, y), t, 255, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        if mode == True:
            cv2.rectangle(img_temp,(x0,y0),(x,y),(0,255,0),3)
            #cv2.rectangle(mask_temp, (ix, iy), (x, y), 255,-1)
            x1,y1 = x,y
        else:
            if ba_fo == False:
                cv2.circle(img_temp, (x, y), t, (0, 0, 0), -1)
                cv2.circle(mask_temp, (x, y), t, 0, -1)
            else:
                cv2.circle(img_temp, (x, y), t, (255, 255, 255), -1)
                cv2.circle(mask_temp, (x, y), t, 255, -1)
    else:
        pass

def get_tar():
    global ba_fo,t,reset,apply
    ba_fo = cv2.getTrackbarPos(switch,'image')
    reset = cv2.getTrackbarPos(switch1,'image')
    apply = cv2.getTrackbarPos(switch2,'image')
    t = cv2.getTrackbarPos('T','image')



cv2.namedWindow('image')

# create trackbars for thickness
cv2.createTrackbar('T','image',0,20,nothing)

# create switch for ON/OFF functionality
switch = '0 : background \n1 : foreground'
cv2.createTrackbar(switch, 'image',0,1,nothing)

switch1 = '0 : ok \n1 : reset'
cv2.createTrackbar(switch1, 'image',0,1,nothing)

switch2 = '0 : draw \n1 : apply'
cv2.createTrackbar(switch2, 'image',0,1,nothing)

cv2.setMouseCallback('image', draw_label)

while(1):
    cv2.imshow('image',img_temp)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('m'):
        mode = not mode

    get_tar()

    if reset == 1:
        img_temp = img.copy()
        img_real = img.copy()
        mask_temp = mask.copy()
        mask_real = mask.copy()
    else:
        pass

    if apply == 1:
        if mode == True:
            rect = (x0,y0,x1-x0,y1-y0)
            cv2.grabCut(img, mask_real, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
            mask_real= np.where((mask_real == 2) | (mask_real == 0), 0, 1).astype('uint8')
            img_real = img * mask_real[:, :, np.newaxis]
            img_temp = img_real.copy()

        else:
            cv2.imwrite('E:\python\opencv\lena_mask.jpg',mask_temp)
            newmask = cv2.imread('E:\python\opencv\lena_mask.jpg',0)

            mask_real[newmask == 0] = 0
            mask_real[newmask == 255] = 1

            mask_real, bgdModel, fgdModel = cv2.grabCut(img, mask_real, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)
            mask_real = np.where((mask_real == 2) | (mask_real == 0), 0, 1).astype('uint8')

            img_real = img * mask_real[:, :, np.newaxis]
            img_temp = img_real.copy()

    else:
        pass


cv2.destroyAllWindows()