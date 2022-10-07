import pandas as pd
import numpy as np

def preprocess(cam_list):
    # Let's replace the empty strings with NaN values
    cam_list = cam_list.replace(' ', np.nan)
    # Let's replace the question marks (?) with NaN values
    cam_list = cam_list.replace('?', np.nan)
    # Let's replace the question marks (.) with NaN values
    cam_list = cam_list.replace('.', np.nan)
    # Let's replace \N (always add an extra forward class)-> (\\N) with NaN values
    cam_list = cam_list.replace('\\N', np.nan)
    
    return cam_list

