# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

                                                                          
import cv2
import numpy as np
img_rgb = cv2.imread('example.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
h , w = img_gray.shape


def non_max(row ):
    c = [] 
    points = []
    result  = []
    co = row.copy() 
    for i  in range(len(row)):
        if co[i] != ():
            c.append(row[i])
            for j  in range(len(row)):
                if co[j] != ():
                    if(abs(row[i][0 ] - row[j][0] )< 5 and abs(row[i][1 ] - row[j][1]) < 5 ):
                        c.append(row[j])
                        co[j] = ()
                        
            points.append(c) 
            co[i] =()
            c=[]
    for p in  points: 
        l = len(p) 
        x = 0 
        y = 0 
        for t in p:
            x+=t[0 ] 
            y += t[1]
        result.append((x/l , y/l , p[0][2]) )   
    return result            

                
result = [ ]    
for i in range(10):
    row =[]
    template = cv2.imread( str(i)+'.png' , 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = .9
    loc = np.where(res >= threshold)  # cv2.minMaxLoc(res)     
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        row.append((pt[0] ,pt[1] , i))
    result+= non_max(row)   
result = sorted(result , key=lambda p: (  p[1] ,p[0])  )


for i  in range(0,200,10):
    x = sorted(result[i:i+10] , key=lambda p: (  p[0] ,p[1])) 
    for ele in  x: 
        print(ele[2] , end='')
    print()             
cv2.namedWindow("res", cv2.WINDOW_NORMAL)
cv2.resizeWindow("res", 500, 500)
cv2.imshow("res", res)
cv2.namedWindow("img_rgb", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img_rgb", 1000, 1000)
cv2.imshow("img_rgb", img_rgb)
cv2.waitKey()

