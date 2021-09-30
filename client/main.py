from pythonping import ping
from datetime import datetime


threshold = 50.0

def checkForLatencyChange(latency):
    if latency > threshold:
        return datetime.now()
    else:
        return None


if __name__ == '__main__':
    ping("google.com", verbose=True)
    
