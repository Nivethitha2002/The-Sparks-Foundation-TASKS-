
#Import the installed libraries:

import cv2 as cv
import pandas as pd
import numpy as np

#Define Image
img = cv.imread("download.jfif")
imgWidth = img.shape[1] - 40

#Teaching the Colors
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv("colors.csv", header=None, names=index)

#Global Variables
clicked = False
r = g = b = xpos = ypos = 0

#Color Recognition Function
r = g = b = xpos = ypos = 0
def getRGBvalue(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    xpos = x
    ypos = y
    b,g,r = img[y,x]
    b = int(b)
    g = int(g)
    r = int(r)

#Mouse Click Function
def colorname(B,G,R):
    minimum = 10000
    for i in range(len(df)):
        d = abs(B-int(df.loc[i,"B"])) + abs(G-int(df.loc[i,"G"])) + abs(R-int(df.loc[i,"R"]))
        if (d<=minimum):
            minimum = d
            cname = df.loc[i,"color_name"] + "Hex" + df.loc[i, "hex"]
    return cname

#The Application
cv.namedWindow("Image")
cv.setMouseCallback("Image",getRGBvalue)
            
while True:
    cv.imshow("Image", img)
    cv.rectangle(img, (20,20), (imgWidth, 60),(b,g,r), -1)
    text = colorname(b,g,r) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    cv.putText(img,text, (50,50),2, 0.8, (255,255,255),2,cv.LINE_AA)    
    if(r+g+b >= 600):
        cv.putText(img,text,(50,50), 2, 0.8, (0,0,0),2,cv.LINE_AA)   
    if cv.waitKey(20) & 0xFF == 27:
        break
    
cv.destroyAllWindows()
