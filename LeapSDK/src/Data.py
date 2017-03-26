import ctypes

frame = controller.frame()

s_tuple = frame.serialize
s_data = s_tuple[0]
s_length = s_tuple[1]
data_address = s_data.cast().__long__()
buffer = (ctypes.c_ubyte * s_length).from_address(data_address)
with open(os.path.realpath('frame.data'), 'wb') as data_file:
    data_file.write(buffer)
