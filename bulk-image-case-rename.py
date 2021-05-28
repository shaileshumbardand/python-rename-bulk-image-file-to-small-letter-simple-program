import os
from tqdm import tqdm

path = 'original/'
output_path = 'output/'

def image_rename():
    cnt = 1
    for img in tqdm(os.listdir(path)):
        if os.path.isfile(path+img):
            filename, file_extention = os.path.splitext(path+img)
            os.rename(os.path.join(path, img), os.path.join(output_path,img.lower() + file_extention))
        cnt +=1
        print(img)

image_rename()
