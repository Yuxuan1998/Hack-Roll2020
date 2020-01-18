import img_recog
import os

path = "../img/test"
file_list = os.listdir(path)

for i in file_list:
    i_path = os.path.join(path, i)
    print(img_recog(i_path))