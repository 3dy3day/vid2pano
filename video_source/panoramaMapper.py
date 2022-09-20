import cv2
import os
import random, string


def randomName():
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
   return ''.join(randlst)

def imageLoader(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            print(filename)
    return images

def main():
    stitcher = cv2.Stitcher.create(0)
    frames = imageLoader("./frames/")
    print("Stitching Frames....(This May Take a While)")
    status, stitched = stitcher.stitch(frames)

    try:
        image_name = f"panoimage_{randomName()}.png"
        cv2.imwrite("./output/"+image_name, stitched)
        return image_name
    except Exception as e:
        print(status, e)