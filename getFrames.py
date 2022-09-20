import cv2
import numpy as np


def m_slice(path, dir, step, extension):
    movie = cv2.VideoCapture(path)
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
    path_head = dir + '\out_'
    ext_index = np.arange(0, Fs, step)
 
    for i in range(Fs - 1): 
        flag, frame = movie.read()
        check = i == ext_index
        
        if flag == True:
            if True in check:
                if i < 10:
                    path_out = path_head + '0000' + str(i) + extension
                elif i < 100:
                    path_out = path_head + '000' + str(i) + extension
                elif i < 1000:
                    path_out = path_head + '00' + str(i) + extension
                elif i < 10000:
                    path_out = path_head + '0' + str(i) + extension
                else:
                    path_out = path_head + str(i) + extension
                cv2.imwrite(path_out, frame)
            else:
                pass
        else:
            pass
    return

def main(source):
    m_slice(source, './frames/', 10, '.png')