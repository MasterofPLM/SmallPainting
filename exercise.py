import cv2
import os

def merge(img1,img2):
    row1,col1,ch1 = img1.shape
    row2,col2,ch2 = img2.shape
    if row1>row2:
        img2 = cv2.copyMakeBorder(img2, (row1 - row2) / 2, row1 - row2 - (row1 - row2) / 2, 0,0, cv2.BORDER_CONSTANT, 255)
    elif row1<row2:
        img1 = cv2.copyMakeBorder(img1, (row2 - row1) / 2, row2 - row1 - (row2 - row1) / 2, 0, 0, cv2.BORDER_CONSTANT, 255)
    else:
        pass

    if col1>col2:
        img2 = cv2.copyMakeBorder(img2, 0, 0, (col1 - col2) / 2, col1 - col2 - (col1 - col2) / 2, cv2.BORDER_CONSTANT, 255)
    elif col1<col2:
        img1 = cv2.copyMakeBorder(img1, 0, 0, (col2 - col1) / 2, col2 - col1 - (col2 - col1) / 2, cv2.BORDER_CONSTANT, 255)
    else:
        pass
    return img1,img2

dir = 'E:\python\opencv\show'
dirlist = []
for dirname in os.listdir(dir):
    dirlist.append(dir+'\\'+dirname)
length = len(dirlist)
i = 0
cv2.namedWindow('ppt')
while(cv2.waitKey(100) & 0xFF != 27):
    if i == length:
        i = 0
    temp1 = cv2.imread(dirlist[i])
    temp2 = cv2.imread(dirlist[(i+1)%length])
    img1 = merge(temp1,temp2)[0]
    img2 = merge(temp1,temp2)[1]
    for j in range(100):
        img = cv2.addWeighted(img1,float(100-j)/float(100),img2,float(j)/float(100),0)
        cv2.imshow('ppt',img)
        cv2.waitKey(10)
    i += 1
    cv2.waitKey(1000)

cv2.destroyAllWindows()