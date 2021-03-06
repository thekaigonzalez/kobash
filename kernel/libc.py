import ctypes
import ctypes.util
import kernel.processor as pla
import os

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)

def mount(source, target, fs, options=''):
    if not pla.is_windows:
        ret = libc.mount(source.encode(), target.encode(), fs.encode(), 0, options.encode())
        if ret < 0:
            errno = ctypes.get_errno()
            raise OSError(errno, f"Error mounting {source} ({fs}) on {target} with options '{options}': {os.strerror(errno)}")
    else:
        return;