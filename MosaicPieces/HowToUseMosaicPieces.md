# Guide To Using MosaicPieces Directory

- Import the `ControlPieces` module
- Call the `ControlPieces.getMosaic()` function
- In the above function, the first argument is the numpy array storing the image and second argument is the number of pieces you want on the mosaic

## Example code 

```python
import sys
import cv2
import numpy as np

sys.path.append ('MosaicPieces')

import ControlPieces as CT

pic = cv2.imread ('Images/hibiscus-1.jpg')

pieces = int (input ('Input the number of pieces you want : '))

mosaicPiece = CT.getMosaic (pic, pieces)

cv2.namedWindow ('pic', cv2.WINDOW_NORMAL)
cv2.imshow ('pic', mosaicPiece)
cv2.waitKey (0)
```