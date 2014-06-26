from ctypes import *
#load zmq library
zmq = cdll.LoadLibrary('/usr/local/lib/libzmq.dylib')

class _Message(Structure):
  _fields_ = [("_", c_ubyte * 32)]

#restypes
zmq.zmq_ctx_new.restype = c_void_p
zmq.zmq_socket.restype = c_void_p
zmq.zmq_setsockopt.restype = c_int
zmq.zmq_bind.restype = c_int
zmq.zmq_send.restype = c_int
zmq.zmq_msg_init.restype = c_int

#argtypes
zmq.zmq_socket.argtypes = [c_void_p, c_int]
zmq.zmq_setsockopt.argtypes = [c_void_p, c_int, c_void_p, c_size_t]
zmq.zmq_bind.argtypes = [c_void_p, c_char_p]
zmq.zmq_send.argtypes = [c_void_p, c_void_p, c_size_t, c_int]
zmq.zmq_msg_init.argtypes = [POINTER(_Message)]

class Message(object):
  def __init__(self):
    self.msg = _Message()
    zmq.zmq_msg_init(byref(self.msg))

class Context(object):
  def __init__(self):
    self.ptr = zmq.zmq_ctx_new()
    self.sockets = []

class Socket(object):
  def __init__(self, context, sock_type):
    self.ptr = zmq.zmq_socket(context.ptr, sock_type)
    self.alive = True
    context.sockets.append(self)
    zmq.zmq_setsockopt(self.ptr, 28, 100, 0)

  def bind(self, endpoint):
    ret = zmq.zmq_bind(self.ptr, endpoint.encode())
    if ret != 0:
      print('zmq error')

  def send_msg(self, msg, flag=0):
    if self.alive:
      ret = zmq.zmq_send(self.ptr, msg.encode(), len(msg), flag)
      return ret
    else:
      return 0