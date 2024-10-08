import ctypes,os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))
_embhash = ctypes.cdll.LoadLibrary("{}/libmurmur3.so".format(dir_path))
def murmur32_128(number,seed):
    global _embhash
    
    c_int32_p_ty = ctypes.POINTER(ctypes.c_int32)

    wrapped_key = ctypes.c_int32(number)
    key = ctypes.cast(ctypes.addressof(wrapped_key), c_int32_p_ty)
    
    len = ctypes.c_int32(4)

    seed = ctypes.c_int32(seed)

    np_output_array = np.arange(3,dtype=np.int32)
    output = np_output_array.ctypes.data_as(c_int32_p_ty)
    #output = ctypes.cast(ctypes.addressof(wrapped_output), c_int128_p_ty)

    _embhash.MurmurHash3_x86_128(key,len,seed,output)
    
    return 
def murmur32_32(number,seed):
    global _embhash
    
    c_int32_p_ty = ctypes.POINTER(ctypes.c_int32)

    wrapped_key = ctypes.c_uint32(number)
    key = ctypes.cast(ctypes.addressof(wrapped_key), c_int32_p_ty)
    
    len = ctypes.c_int32(4)

    seed = ctypes.c_uint32(seed)

    wrapped_output = ctypes.c_uint32(0)
    output = ctypes.cast(ctypes.addressof(wrapped_output), c_int32_p_ty)

    _embhash.MurmurHash3_x86_32(key,len,seed,output)
    ret = output.contents.value
    ret &= 0xffffffff
    return ret
if __name__ == '__main__':
    ret = murmur32_32(0x08001904,0x3bb8993d)
    idx = ret % 119 
    print( ret, idx)
