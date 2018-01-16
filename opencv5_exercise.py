# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:37:16 2018
OpenCV-Python Tutorials » Gui Features in OpenCV » Trackbar as the Color Palette
@author: zzx_pc
"""

"""
cv2.createTrackbar()
第一个参数是trackbar名称，
第二个参数是窗口名称，
第三个参数是默认值，
第四个参数是最大值，
第五个参数是执行的回调函数,回调函数总是有一个默认的参数是trackbar的位置
注意：此函数除了滑动条还可以创建开关
cv2.getTrackbarPos（）两个参数：trackbar名称和窗口名
"""

import cv2
import numpy as np

draw = False

def nothing(x):
    pass

def draw_line(event,x,y,flags,param):
    global draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.circle(img, (x,y),t,(b,g,r),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
    else:
        pass

def get_tar():
    global r,g,b,s,t
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    t = cv2.getTrackbarPos('T','image')

# Create a black image, a window
img = np.zeros((300,512,3),np.uint8)
img[:] = 255
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('T','image',0,20,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)
cv2.setMouseCallback('image', draw_line)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    get_tar()

    if s == 0:
        img[:] = 255
        draw = False
        
cv2.destroyAllWindows()