import os
import cv2
import sys
import glob


def resize(path_to_file):
    print(path_to_file)
    
    
    scaleFactor = 0.95
    
    if not os.path.exists(path_to_file):
        print('File not found')
        return
    img = cv2.imread(path_to_file, cv2.IMREAD_UNCHANGED)

    filename = path_to_file.split('/')[-1]
    
    filename = filename.split(".")[0]



    # 1300 and 800 are arbitrary size that fits in a full screen gui
    x,y = len(img[1]),len(img[0])
    while x > 1300 or y > 800: x,y = x*scaleFactor,y*scaleFactor
    
    resized = cv2.resize(img,(int(x),int(y)),interpolation = cv2.INTER_AREA)
    cv2.imwrite("./Images/deadpool/"+filename+".jpg",resized)
    

for image in glob.glob("./Images/deadpool_old/*"):
    resize(image)