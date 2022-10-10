import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve']  #__all__ specifies all modules that shall be loaded and imported into the current namespace when us use from package import * 


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b
