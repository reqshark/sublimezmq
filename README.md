sublimezmq
==========

### Sublime Text C language binding to zeromq 

Low latency, low footprint zeromq messaging delivered by Sublime Text 3. 

What this is not
------------
This is not [pyzmq](https://github.com/zeromq/pyzmq). Lame, why not just use pyzmq and import it to a Sublime Text plugin? 

Sublime runs it's own zipped version of the Python interpreter. Word up. 

Pyzmq was not included in the Sublime Text bundled Python environment. This makes sense because libzmq has to be compiled. 

The sublimezmq package circumverts all attempts to install and import pyzmq bindings from directly within our favorite Text Editor's unique interpreter.

Basic Kernel Requirements
------------
1. Darwin. Tested on OS X 10.10 and 10.9 (nothing else tested yet). Linux and Windows compatibility coming right up after package control distribution/installation.

2. Zeromq Messaging library installed (make sure to at least have it sym linked) at /usr/local/lib/libzmq.dylib. This dependency is temporary, and it would be more preferable to follow Sublime Plugin conventions with a default and user `sublime.settings` config file so you can tell sublime where to find your zmqlib.

I recommend using `brew install zeromq` if you don't feel like compiling libzmq.


Installation
------------
confirm that your compiled version of libzmq works.

from the Packages directory git clone:

``` bash
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
$ git clone https://github.com/reqshark/sublimezmq.git
```

Now what
------------
Sublime Text 3 now publishes the file name and path of any file you save locally over a unix socket. 

This is my preference over having the built in python interpreter open a subprocess shell for special interaction.

Now connect a basic zmq subscriber without any special options. 

Set your local zeromq process subscription over a unix socket at `ipc:///tmp/sublime`. It doesnt matter how you like to use libzmq.

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

(The MIT License)

Copyright (c) 2014 Bent Cardan &lt;bent@nothingsatisfies.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
