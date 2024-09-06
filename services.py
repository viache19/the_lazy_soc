import platform
import os
import psutil
import socket
import sys
import tempfile

from math import log, pow
def readable_size(size_in_bytes):
    """Convert the bytes for human readable format (KB, MB, GB, etc.)."""
    if size_in_bytes == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(log(size_in_bytes, 1024))
    p = pow(1024, i)
    s = round(size_in_bytes / p, 2)

    return "%s %s" % (s, size_name[i])

def print_system_information():
    print("System info: ")
    print("-" * 30)

    print("OS: ", platform.system())
    print("OS version: ", platform.version())
    print("Network node:", platform.node())
    print("System name:", platform.machine())
    print("CPU:", platform.processor())
    print("Python Version:", platform.python_version())

    print("\nActual directory:", os.getcwd())
    print("Global Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

    print("\nCPU usage: ")
    print("  Percentage: ", psutil.cpu_percent(interval=1), "%")
    print("  Nº of cores: ", psutil.cpu_count(logical=False))

    print("\nRAM usage: ")
    memory = psutil.virtual_memory()
    print("  Total:", readable_size(memory.total))
    print("  Available:", readable_size(memory.available))
    print("  Used:", readable_size(memory.used))

    print("\nDisk usage: ")
    disk = psutil.disk_usage('/')
    print("  Total:", readable_size(disk.total))
    print("  Available/Free: ", readable_size(disk.free))
    print("  Used:", readable_size(disk.used))

    print("\nNetwork info:")
    print("Hostname:", socket.gethostname())
    print("Local IP:", socket.gethostbyname(socket.gethostname()))

    print("\nPython environment ifo:")
    print("Python Version:", sys.version)
    print("Platform:", sys.platform)
    print("Python sys path:", sys.path)
