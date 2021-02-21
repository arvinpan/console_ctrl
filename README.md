# Console CTRL

This simple package allows you to send CTRL-C event to a target console process WITHOUT causing KeyboardInterrput at the caller side.

The solution is based on posts shared on stackoverflow (see Reference for details).

## Usage

Install with `pip install console-ctrl`

In you code:

```python
import console_ctrl
import subprocess

# Start some command IN A SEPARATE CONSOLE
p = subprocess.Popen(['some_command'], creationflags=subprocess.CREATE_NEW_CONSOLE)
# Do something else

console_ctrl.send_ctrl_c(p.pid)
```

Note: the target process should be started with `creationflags=subprocess.CREATE_NEW_CONSOLE`.

## Reference

Specially thanks to people shared solutions here:

- https://stackoverflow.com/questions/7085604/sending-c-to-python-subprocess-objects-on-windows
- https://stackoverflow.com/questions/813086/can-i-send-a-ctrl-c-sigint-to-an-application-on-windows

More official docs:

- https://docs.microsoft.com/en-us/windows/console/generateconsolectrlevent
- https://docs.python.org/3/library/subprocess.html
