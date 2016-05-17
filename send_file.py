# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:20:18 2015

@author: antariksh
"""
# Server 
import socket

def main():
    s = socket.socket()
    # host name == ''-> all connections accepted 
    host = ''#socket.gethostname() 
    port = 6000
    s.bind((host,port))
    s.listen(5)
    filename=raw_input('Enter Filename:')
    f=open(filename,'rb')  # reading file in binary format    
    c, addr = s.accept()
    print 'Got Connected to', addr, c
    i=0    
    while True:
        str = f.read(1024)
        if str=='':
            break
        #temp=c.recv(1)        
        c.send(str)        
        i=i+1        
        #print str
    """
    for line in f:
        print line
        c.send(line)
        print c.recv(5)
    """
    print 'Done ',i
    f.close()
    c.close
    s.close
    

if __name__ == '__main__':
    main()
