#! /usr/bin/python
from multiprocessing import Process
import socket
import sys
import os

import shelve

import cossineSim

#open the persisted indexes
#This is a server to a tfidf index
#TODO: create and shelve these indexes
#We need the inverted index to weight the query terms
idfIndex = shelve.open('idfIndex.db')['1']
tfidfIndex = shelve.open('tfidfIndex.db')['1']

BUFLEN = 256




#TODO: implement using Ravi's code from github
#def queryVector (rawQuery):



# handle every client in a separate subprocess
# to facilitate multiple clients simultaneously
def handleClientRequest(info, sock_obj, data_root_directory):
        print 'Accepted connection from client: '
        print '%s, port: %s' % (info[0], info[1])
        print '\n'
        data = ''
#        while(True):
        tempData = sock_obj.recv(BUFLEN)
            #if not tempData:
             #   break
        data += tempData

	#this is a query string 
	print 'The data sent to the server was: %s' % data
        #parse query and get a dictionary query[word] = tfidf value
	query = queryVector(data)#should this be salsa.querySalsa(data)?
	print 'query vector is: %s' %str(query) 
	#result = [(56193, 'Page'), (35272, 'sheet'), (6171, 'side')]
	
	
	noSyn = 0
        for syn in result:
		 #if the score is not 0
		score = syn[0] 
		if (score > 0):
		 	output += '|' + syn[1]
			noSyn += 1
	if (noSyn > 0):
		sock_obj.sendall(output+"\n")
	else:
		empty = 'No synonyms were found...'
		sock_obj.sendall(empty+"\n")
	
        print 'The result from salsa was: %s' % output 	
	#Update: can't send a list - needs to be a single string (currently | delimited)
       	sock_obj.sendall(output+"\n")
	print 'Closing Connection'
        sock_obj.close()

        #fDirName = data_root_directory + '/' + str(info[0]) + '_' + str(info[1]) + '/'
        #os.mkdir(fDirName)
        #os.chdir(fDirName)
        #f = open('data.txt', 'wb')
        #f.write(data)
        #f.close()

        #os.chdir('..')
        #print 'Data transferred to %s' % fDirName

def startServer(port_number, data_root_directory):
    server_sock = socket.socket()
    server_sock.bind(('127.0.0.1', int(port_number)))
    server_sock.listen(0)
    while(True):
        # Accept a connection
        sock_obj, info = server_sock.accept()
        # Create a subprocess to deal with the client
        process = Process(target = handleClientRequest, args=(info, sock_obj, data_root_directory))
        process.start()
        process.join()

def error():
    print 'Usage: ./server.py port_number data_root_directory'
    print 'Exiting ... '
    sys.exit()

def main():
    if len(sys.argv) != 3:
        error()
    startServer(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
