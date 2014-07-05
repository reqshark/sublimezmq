from ctypes import *

zmq = cdll.LoadLibrary('/usr/local/lib/libzmq.dylib')

class _Message(Structure):
  _fields_ = [('_', c_ubyte * 32)]

#introduce zmq ctx and return types
zmq.zmq_ctx_new.restype = c_void_p
zmq.zmq_socket.restype = c_void_p
zmq.zmq_setsockopt.restype = c_int
zmq.zmq_connect.restype = c_int
zmq.zmq_bind.restype = c_int
zmq.zmq_send.restype = c_int
zmq.zmq_msg_init.restype = c_int
zmq.zmq_msg_recv.restype = c_int
zmq.zmq_msg_size.restype = c_size_t
zmq.zmq_msg_data.restype = c_char_p
zmq.zmq_msg_close.restype = c_int

#corresponding arg types
zmq.zmq_socket.argtypes = [c_void_p, c_int]
zmq.zmq_setsockopt.argtypes = [c_void_p, c_int, c_void_p, c_size_t]
zmq.zmq_connect.argtypes = [c_void_p, c_char_p]
zmq.zmq_bind.argtypes = [c_void_p, c_char_p]
zmq.zmq_send.argtypes = [c_void_p, c_void_p, c_size_t, c_int]
zmq.zmq_msg_init.argtypes = [POINTER(_Message)]
zmq.zmq_msg_recv.argtypes = [POINTER(_Message), c_void_p, c_int]
zmq.zmq_msg_data.argtypes = [POINTER(_Message)]
zmq.zmq_msg_size.argtypes = [POINTER(_Message)]
zmq.zmq_msg_close.argtypes = [POINTER(_Message)]

class Context(object):
  def __init__(self): self.pointer = zmq.zmq_ctx_new(); self.sockets = [];

class Message(object):
  def __init__(self): self._m = _Message(); zmq.zmq_msg_init(byref(self._m));

class Socket(object):
  def __init__(self,ctx,socket_integer):
    self.pointer = zmq.zmq_socket(ctx.pointer,socket_integer)
    ctx.sockets.append(self)
    if socket_integer == 1: zmq.zmq_setsockopt(self.pointer, 28, 100, 0)
    else: zmq.zmq_setsockopt(self.pointer, 6, b'', 0)

  def msg_struct(self):
    m = Message();zmq.zmq_msg_recv(byref(m._m),self.pointer,2)
    zmq_string = zmq.zmq_msg_data(byref(m._m))[:zmq.zmq_msg_size(byref(m._m))].decode()
    zmq.zmq_msg_close(byref(m._m))
    return zmq_string

  def send_msg(self, msg, flag=0):
    return zmq.zmq_send(self.pointer, msg.encode(), len(msg), flag)

  def bind(self, endpoint):
    return zmq.zmq_bind(self.pointer, endpoint.encode())

  def connect(self, endpoint):
    return zmq.zmq_connect(self.pointer, endpoint.encode())