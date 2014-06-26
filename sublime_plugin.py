import sublime, sublime_plugin
from . import zmq

#pass zmq kernel context to a pub socket
pub = zmq.Socket(zmq.Context(),1);

#bind over local unix sock
pub.bind('ipc:///tmp/sublime');

class Save(sublime_plugin.EventListener):
  def on_post_save(self,view):
    #publish file_name after editor save event
    pub.send_msg(str(view.file_name()),1);