import numpy as np
import struct 


class NumPyCreator:
    
    def __init__(self):
        pass


    def from_list(self, lst, **kwargs):
        # buffer = np.array(lst, dtype=object)
        # return np.ndarray(shape=buffer.size, buffer=buffer, dtype=dtype)
        print(dtype)
        lst = [item for sublist in lst for item in sublist]
        buffer = struct.pack('i'*len(lst), *lst)
        return np.ndarray(shape=(len(lst),), buffer=buffer, dtype=dtype)
        # return np.ndarray(shape=(len(lst),), buffer=bytes(np.frombuffer(lst, dtype=dtype)), dtype=dtype)
        # return np.array(lst, dtype=object)

    def from_tuple(self, tpl, dtype=None):
        pass

    def from_iterable(self, itr, dtype=None):
        pass

    def from_shape(self, shape, value, dtype=None):
        pass

    def random(self, shape, dtype=None):
        pass

    def identity(self, n, dtype=None):
        pass

