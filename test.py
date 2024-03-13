import ctypes
import time
f = ctypes.CDLL("./libtest.so").rapid_mult
f.restype = ctypes.c_void_p
f.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
from vector import Vector

vec_1 = Vector.fromList([i for i in range(1000)])
vec_2 = Vector.fromList([i for i in range(1000)])
start = time.time()
vec_3 = Vector.fromVector(f(vec_1.vector, vec_2.vector))
end = time.time()

print(end-start)

li1 = [i for i in range(1000)]
li2 = [i for i in range(1000)]
start = time.time()
li3 = []
for i in range(1000):
    li3.append(li1[i]*li2[i])
end = time.time()
print(end-start)