import platform
import menu
def detect_os():
    system = platform.system()
    if system == "Windows":
        return "It is Windows"
    elif system == "Darwin":
        return "It is MacOs"
    elif system == "Linux":
        return "It is Linux"
    else:
        return "OS not identified"

menu.menu()

