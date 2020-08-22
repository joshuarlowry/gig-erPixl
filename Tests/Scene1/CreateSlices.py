from PIL import Image
import math

def cropit(shiftx, shifty, idx):
    box = (width/shiftx-picamres[0]/2,height/shifty-picamres[1]/2,width/shiftx+picamres[0]/2,height/shifty + picamres[1]/2)
    im_crop = im.crop(box)
    im_crop.save('.\\Tests\\Scene1\\Slices\\'+str(idx)+'.jpg', quality=100)

picamres = (2592, 1944)
im = Image.open(".\\Tests\\Scene1\\ben-yubqG1fDF7I-unsplash.jpg")

width, height = im.size

print(width, height)
widthSteps = math.ceil(width/picamres[0])*2
heightSteps = math.ceil(height/picamres[1])*2
# print(math.ceil(widthSteps))
# print(math.ceil(heightSteps))

widthStep = width/widthSteps
heightStep = height/heightSteps

cropit(1.5,1.5,1)
cropit(2,2,2)
cropit(3,3,3)
cropit(1.5,2,4)
cropit(1.5,3,5)
cropit(3,1.5,6)
cropit(3,2,6)