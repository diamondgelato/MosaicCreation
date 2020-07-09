import cv2
import numpy as np
import random as rd
import TriangulationTest as TT


def drawPoly(pic, drawPoints, matchPoints, lineWt):
    for Pt in drawPoints:
        counter = 0

        # finds the not matched point of the triangle
        for Pt1 in matchPoints:
            if Pt != Pt1:
                counter += 1

        # draws the lines of the merged shape
        if counter == 2:
            pic = cv2.line(pic, Pt, matchPoints[0], (0, 0, 0), lineWt)
            pic = cv2.line(pic, Pt, matchPoints[1], (0, 0, 0), lineWt)


def getMosaicPieces(pic, noOfInsidePoints, noOfEdgePoints, noOfPieces, lineWt):
    trianglesMerged = []
    noOfTri, triangles = TT.getTriangles(pic, noOfInsidePoints, noOfEdgePoints)
    length = triangles.shape[0]
    merged = 0

    if noOfPieces == 0: 
        # for random number of triengles joined
        noOfMergedTri = int ((1/3) * noOfTri)
    elif noOfPieces == -1:
        # for no triangles joined
        noOfMergedTri = 0
    elif noOfPieces > 0:
        # for getting to required number of pieces
        noOfMergedTri = (noOfTri - noOfPieces)

    # number of triangles to be merged
    while merged < noOfMergedTri:
        while True:
            isRepeat = 0
            randIndex = rd.randint(0, length-1)

            for t in trianglesMerged:
                if t == randIndex:
                    isRepeat = 1
            
            if (isRepeat == 0):
                break

        randTri = triangles[randIndex]
        ogPts = [(randTri[0], randTri[1]),
                 (randTri[2], randTri[3]),
                 (randTri[4], randTri[5])]
        matchedTriangles = 0

        # loop going through all triangles
        for j in range(0, length):
            t = triangles[j]
            pt1, pt2, pt3 = (t[0], t[1]), (t[2], t[3]), (t[4], t[5])
            checkPts = [pt1, pt2, pt3]
            matchedPoints = []
            ptMatched = 0

            # check adjacent triangles
            for Pt in ogPts:
                for Pt1 in checkPts:
                    if Pt == Pt1:
                        ptMatched += 1
                        matchedPoints.append(Pt)
                        break

            if (ptMatched == 2) and (matchedTriangles == 0) and (not(j in trianglesMerged)):
                # found an adjacent triangle
                trianglesMerged.append(randIndex)
                trianglesMerged.append(j)
                matchedTriangles += 1

                # draw the merged shape
                drawPoly(pic, checkPts, matchedPoints, lineWt)
                drawPoly(pic, ogPts, matchedPoints, lineWt)
                merged += 1

    # Drawing the triangles

    for i in range(0, length):
        isMerged = 0

        for t1 in trianglesMerged:
            if ((triangles[i] == triangles[t1]).all()):
                isMerged = 1

        if isMerged == 0:
            t = triangles[i]
            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])

            pic = cv2.line(pic, pt1, pt2, (0, 0, 0), lineWt)
            pic = cv2.line(pic, pt2, pt3, (0, 0, 0), lineWt)
            pic = cv2.line(pic, pt1, pt3, (0, 0, 0), lineWt)

    return (noOfTri, pic)
