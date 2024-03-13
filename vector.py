import ctypes

class Vector(object):
    lib = ctypes.CDLL('_vector.so')
    lib._create.restype = ctypes.c_void_p
    lib._create.argtypes = []
    lib._delete.restype = None
    lib._delete.argtypes = [ctypes.c_void_p]
    lib._size.restype = ctypes.c_int
    lib._size.argtypes = [ctypes.c_void_p]
    lib._get.restype = ctypes.c_int
    lib._get.argtypes = [ctypes.c_void_p, ctypes.c_int]
    lib._push_back.restype = None
    lib._push_back.argtypes = [ctypes.c_void_p, ctypes.c_int]

    class IntArray(object):
        def __init__(self):
            self.vector = Vector.lib._create()
        def __del__(self):
            Vector.lib._delete(self.vector)
        def __len__(self):
            return Vector.lib._size(self.vector)
        def __getitem__(self, i):
            if 0 <= i < self.__len__():
                return Vector.lib._get(self.vector, ctypes.c_int(i))
            raise IndexError(f'Index {i} out of range for IntArray with size of {self.__len__()}')
        def __iter__(self):
            for i in range(self.__len__()):
                yield self.__getitem__(i)
        def __repr__(self):
            return f"[{', '.join(str(i) for i in self)}]"
        def append(self, i):
            Vector.lib._push_back(self.vector, ctypes.c_int(i))
    
    def fromList(li):
        arr = Vector.IntArray()
        for i in li:
            arr.append(i)
        return arr

    def fromVector(vec):
        arr = Vector.IntArray()
        arr.vector = vec
        return arr

