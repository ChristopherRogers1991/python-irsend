# python-irsend

This is a simple wrapper for [lirc's irsend](http://www.lirc.org/html/irsend.html).

## Basic Usage:

```
>>> from irsend import irsend
>>> irsend.list_remotes()
['lasko_heater', 'lights.conf', 'dynex_tv', 'logitech_z906', 'sabrent_hdmi_switch']
>>> irsend.list_codes('logitech_z906')
['POWER', 'INPUT', 'MUTE', 'LEVEL', 'EFFECT', 'VOLUME_DOWN', 'VOLUME_UP']
>>> irsend.send_once('logitech_z906', ['POWER'])
```

It makes use of [subprocess](https://docs.python.org/2/library/subprocess.html)
to call irsend. No attempts are made to handle errors (e.g. irsend not being
installed, or lircd not running), and instead leaves those to the caller. See
the documentation for subprocess (specifically
[check_call](https://docs.python.org/2/library/subprocess.html#subprocess.check_call) and
[check_output](https://docs.python.org/2/library/subprocess.html#subprocess.check_output)
to determine which exceptions may be raised.
