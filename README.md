sublimezmq
==========

### Sublime Text binding

Minimal messaging interface for Sublime Text 3.

## IMPORTANT WARNING ABOUT THIS SOFTWARE:

Make a backup of your Sublime Text application support directory first before you attempt to use this, since this plugin could break some functionality in your sublime text editor. Like it would mess up my ability to create new folders when I was working in other projects one time. So be warned about that: if it is not installed properly or if your system somehow doesn't like it.

If this thing breaks your editor then you'll want to reinstall a fresh sublime with all your package cache, etc. settings from your backed up `Sublime Text 3` directory in application support.

On the macintosh, and its equivalent location on other systems, back up this directory first: `cd ~/Library/Application\ Support/Sublime\ Text\ 3/`

Basic Kernel Setup
------------
1. Darwin. Tested on OS X 10.10 and 10.9

2. libzmq on *nix sym linked at `/usr/local/lib/libzmq.dylib` or just edit [zmq.py](https://github.com/reqshark/sublimezmq/blob/master/zmq.py#L3).

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
var pub = zmq.socket('pub')

//ipc here, so for the windows env just opt for tcp over localhost
sub.connect('ipc:///tmp/sublime')

sub.subscribe('on_post_save')
sub.subscribe('on_modified')
console.log('subscriber bound to `on_post_save` and `on_modified` events')

sub.on('message', function (msg) {
  console.log(String(msg))
});

//pub.bind('ipc:///tmp/sublimezmq',function (err) {
//  if(err)throw err
//  setInterval(function(){
//    var msg = '' + Math.random() * 1000
//    pub.send(msg)
//    console.log('just sent: %s to sublime text', msg)
//  },2000)
//})
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
