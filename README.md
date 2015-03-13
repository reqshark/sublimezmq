sublimezmq
==========

### Sublime Text binding

Minimal messaging interface for Sublime Text 3.

Basic Kernel Setup
------------
1. Darwin. Tested on OS X 10.10 and 10.9

2. libzmq on *nix sym linked at `/usr/local/lib/libzmq.4.dylib` or just edit [zmq.py](https://github.com/reqshark/sublimezmq/blob/master/zmq.py#L3).

3. make sure your particular usr/local libzmq works.

4. Shut off and quit your sublime text 3 editor completely.

5. Then from inside Sublime's Packages directory git clone along these lines:

``` bash
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
$ git clone https://github.com/reqshark/sublimezmq.git && cd sublimezmq
#dont depart sublimezmq dir yet. clean up pkg before turning sublime back on:
$ rm -rf .git && rm History.md && rm README.md
```

Now what
------------
hook Sublime Text 3's `sublime_plugin.EventListener` over zmq sockets.

Here's an example using the [node zeromq bindings](https://github.com/JustinTulloss/zeromq.node). The idea is to efficiently distribute information or events from sublime text:
``` js
var zmq = require('zmq')
var sub = zmq.socket('sub')

sub.connect('tcp://127.0.0.1:64000')

sub.subscribe('on_post_save')
//sub.subscribe('on_modified')
console.log('subscriber connected to `on_post_save` and `on_modified` events')

sub.on('message', function (msg) {
  console.log(String(msg))
});
```

License
-------

This is free and unencumbered software released into the public domain.
