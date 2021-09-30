from pythonping import ping
from datetime import datetime


def checkForLatencyChange(latency):
    return datetime.now()


if __name__ == '__main__':
    ping("google.com", verbose=True)
    
