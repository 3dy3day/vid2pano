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
                path_out = path_head + str(i).zfill(8) + extension
                cv2.imwrite(path_out, frame)
            else:
                pass
        else:
            pass
    return

def main(source):
    m_slice(source, './frames/', 10, '.png')