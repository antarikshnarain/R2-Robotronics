# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:44:12 2015

@author: antariksh
"""
# Client 1
import socket

def main():
    s = socket.socket()
    host = '0.0.0.0'#'192.168.1.5'#socket.gethostname()
    port = 6000
    filename=raw_input('Enter Filename to Save as:')
    f=open(filename,'w')
    s.connect((host,port))
    i=1    
    while True:
        #s.send('1')                
        str=s.recv(1024)        
        #print str, len(str),i        
        f.write(str)        
        i=i+1
        if len(str)==0:
            print 'inside'
            break
    f.write(chr(26))
    print i    
    s.close()
    f.close()
    

if __name__ == '__main__':
    main()
