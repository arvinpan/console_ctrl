import sys
import subprocess


def send_ctrl_c(pid):
    """Send CTRL-C signal to the given process."""
    subprocess.check_call([sys.executable, '-m', 'console_ctrl', str(pid)])
