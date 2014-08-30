sublimezmq
==========

### Sublime Text binding

Minimal messaging interface for Sublime Text 3.

Basic Kernel Setup
------------
1. Darwin. Tested on OS X 10.10 and 10.9

2. libzmq on *nix sym linked at `/usr/local/lib/libzmq.dylib` or just edit [zmq.py](https://github.com/reqshark/sublimezmq/blob/master/zmq.py#L3).

3. make sure your local libzmq works. Then from inside Sublime's Packages directory git clone:

``` bash
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
$ git clone https://github.com/reqshark/sublimezmq.git
```

Now what
------------
hook Sublime Text 3's `sublime_plugin.EventListener` over zmq unix sockets.

Example using the [node zeromq bindings](https://github.com/JustinTulloss/zeromq.node):
``` js
var sub = require('zmq').socket('sub')

sub.connect('ipc:///tmp/sublime');

sub.subscribe('');

sub.on('message', function (msg) {
  console.log(msg.toString());
});
```

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://www.wtfpl.net/>
