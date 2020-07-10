import cv2
import numpy as np
import random as rd

def getTriangles(img, insidePt, edgePt):

    # orig = np.copy (img)
    width = img.shape[1]
    height = img.shape[0]
    rect = (0, 0, width, height)
    subdiv = cv2.Subdiv2D(rect)

    # points on the inside

    for i in range(0, insidePt):
        randx = rd.randint(0, width-1)
        randy = rd.randint(0, height-1)
        subdiv.insert((randx, randy))

    # edge points

    for i in range(0, edgePt):
        subdiv.insert((0, rd.randint(0, height-1)))
        subdiv.insert((rd.randint(0, width-1), 0))
        subdiv.insert((width-1, rd.randint(0, height-1)))
        subdiv.insert((rd.randint(0, width-1), height-1))

    # corners

    subdiv.insert((0, 0))
    subdiv.insert((0, height-1))
    subdiv.insert((width-1, 0))
    subdiv.insert((width-1, height-1))

    triangleList = subdiv.getTriangleList()
    noPieces = triangleList.shape[0]

    return (noPieces, triangleList)

