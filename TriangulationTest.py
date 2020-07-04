import cv2
import numpy as np
import random as rd

img = cv2.imread ("Images/grand-mosque.jpg")
orig = np.copy (img)
width = img.shape [1]
height = img.shape [0]
rect = (0, 0, width, height)
subdiv = cv2.Subdiv2D (rect)

# points on the inside

for i in range (0, 250):
    randx = rd.randint (0, width)
    randy = rd.randint (0, height)
    subdiv.insert ((randx, randy))

# edge points

for i in range (0, 15):                                   
    subdiv.insert ((0, rd.randint(0, height)))
    subdiv.insert ((rd.randint(0, width), 0))
    subdiv.insert ((width-1, rd.randint(0, height)))
    subdiv.insert ((rd.randint(0, width), height-1))

# corners

subdiv.insert ((0, 0))
subdiv.insert ((0, height-1))
subdiv.insert ((width-1, 0))
subdiv.insert ((width-1, height-1))

triangleList = subdiv.getTriangleList ()

for t in triangleList:
    pt1 = (t[0], t[1])
    pt2 = (t[2], t[3])
    pt3 = (t[4], t[5])

    # draws the triangles

    cv2.line (img, pt1, pt2, (0, 0, 0), 15)
    cv2.line (img, pt2, pt3, (0, 0, 0), 15)
    cv2.line (img, pt1, pt3, (0, 0, 0), 15)

cv2.namedWindow ('orig', cv2.WINDOW_NORMAL)
cv2.imshow ('orig', img)
cv2.waitKey (0)
