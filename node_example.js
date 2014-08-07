var zmq = require('zmq');
var sub = zmq.socket('sub');
var pub = zmq.socket('pub');

//ipc is probably a unix/linux domain socket
//so for the windows env just opt for tcp over localhost
sub.connect('ipc:///tmp/sublime');

sub.subscribe('on_post_save');
sub.subscribe('on_modified');
console.log('subscriber bound')

sub.on('message', function (msg) {
  console.log(msg.toString());
});

pub.bind('ipc:///tmp/sublimezmq',function (err) {
  if(err)throw err;
  setInterval(function(){
    var msg = 'hey there:'+Math.random()*1000;
    pub.send(msg);
    console.log('notice: ',msg);
  },2000)
});
