import sublime, sublime_plugin, threading
from . import zmq

def poll_msgs():
  print(sub.msg_struct())
  threading.Timer(1,poll_msgs).start()

class Event(sublime_plugin.EventListener):
  def on_post_save(self,view): pub.send_msg(' '.join(['on_post_save',str(view.file_name())]),1);
  def on_modified(self,view): pub.send_msg(' '.join(['on_modified',str(view.file_name())]),1);
  def on_activated(self,view): pub.send_msg(' '.join(['on_activated',str(view.file_name())]),1);
  def on_deactivated(self,view): pub.send_msg(' '.join(['on_deactivated',str(view.file_name())]),1);

pub = zmq.Socket(zmq.Context(),1);pub.bind('ipc:///tmp/sublime');
sub = zmq.Socket(zmq.Context(),2);sub.connect('ipc:///tmp/sublimezmq');
poll_msgs();