import cv2
import numpy as np
import MergeAdjacentTriangles as MAT


def getMosaic(pic, noOfPieces):

    # decide lineWt based on dimensions
    dim = max(pic.shape[0], pic.shape[1])
    lineWt = int(1.5 * (dim/1000))

    if lineWt == 0:
        lineWt = 1

    # set number of points according to number of pieces input
    defaultInsidePts = 600
    defaultEdgePts = 20
    noOfPieces = int(noOfPieces)

    Map = ((10, 13, 3, 2),
           (13, 15, 5, 2),
           (15, 20, 7, 2),
           (20, 25, 10, 3),
           (25, 35, 15, 3),
           (35, 40, 15, 4),
           (40, 50, 20, 4),
           (50, 63, 25, 5),
           (63, 80, 37, 5),
           (80, 105, 50, 5),
           (105, 130, 65, 5),
           (130, 160, 85, 5),
           (160, 230, 100, 10),
           (230, 320, 150, 10),
           (320, 450, 200, 15),
           (450, 600, 300, 15),
           (600, 750, 400, 20),
           (750, 850, 500, 20),
           (850, 1000, 600, 20),
           (1000, 1250, 700, 20),
           (1250, 1500, 800, 20),)

    if noOfPieces == 0:
        mosaic = MAT.getMosaicPieces(
            pic, defaultInsidePts, defaultEdgePts, noOfPieces, lineWt)[1]
    else:
        for a in Map:
            if noOfPieces > a[0] and noOfPieces <= a[1]:
                mosaic = MAT.getMosaicPieces(
                    pic, a[2], a[3], noOfPieces, lineWt)[1]

    return mosaic
