var sub = require('zmq').socket('sub')

sub.connect('ipc:///tmp/sublime');

sub.subscribe('');

console.log('subscriber bound')

sub.on('message', function (msg) {
  console.log(msg.toString());
});