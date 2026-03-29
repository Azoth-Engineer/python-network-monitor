import os
import platform

def check_server_status(host):
    """
    Azoth-Engineer Network Monitor
    Simple script to check host availability
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 {host}"
    
    return os.system(command) == 0

if __name__ == "__main__":
    target = "8.8.8.8"
    if check_server_status(target):
        print(f"🚀 Host {target} is UP and reachable.")
    else:
        print(f"⚠️ Host {target} is DOWN.")
