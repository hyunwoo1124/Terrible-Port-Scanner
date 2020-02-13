import sys                           # allows you to enter cmd line arguments
import socket                        # THis allows you to use socket programming
from datetime import datetime        # This allows you track time


#Defining our Targets
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument")
    print("Syntax  python3 terribleScannerpy <ip>")
    sys.exit()

# Add a Banner
print("_" * 50)
print("Scanning target " + target)
print("Time Started: " + str(datetime.now()))
print("_" * 50)

try:
    for port in range (0, 1000):
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # 1  is error 0 is good
        print("Checking port {}".format(port))
        if( result == 0):
                print("Port {} is open".format(port))
        s.close()

except keyboardInterrupt:
    print("\nExiting Program...")
    sys.exit()
except socket.gaierror:
    print("Hostname caould not be resolved...")
    sys.exit()
except socket.error:
    print("Couldn't connect to the server...")
    sys.exit()