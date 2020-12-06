import socket
import struct
from machine import RTC
import time 

# (date(2000, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 3155673600

host = "pool.ntp.org"

def getTime():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1b
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    res = s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
    s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    return val - NTP_DELTA

# There's currently no timezone support in MicroPython, so
# utime.localtime() will return UTC time
def setTime(temps,heure="ete"):
    if(heure == "ete"):
        heure = 2
    else:
        heure = 1

    tm = time.localtime(temps + 3600 * heure)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    return tm

def addZeroToTime(clock):
    h = []
    for i in clock:
        if(i < 10):
            h.append("0" + str(i))
        else:
            h.append(str(i))
    return h

def hourStr(l):
    if(int(l[6]) % 2 == 0):
        sep = ":"
    else:
        sep = " "
    h = str(l[4]) + sep + str(l[5])
    return h

def dateStr(l):
    return str(l[2]) + ":" + str(l[1])
