import socket
import sys
import time


#  Do 10 requests, waiting each time for a response
#for request in range (1,4):
#    print "Sending request ", request,"..."
#    socket.send ("C:\Users\Osama Chaudhary\Desktop\oledump\est\docm.docm")
#    message = socket.recv()
#    print "Received reply ", request, "[", message, "]"


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM0.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM1.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM12.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM3.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM4.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM5.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCM6.docm;DOCM")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCX0.docx;DOCX")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCX1.docx;DOCX")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

print "Sending request... "
s.send("C:\Users\Osama Chaudhary\Desktop\Data\DOCX3.docx;DOCX")
print "Sent"
message = s.recv(BUFFER_SIZE)
if not message:
    message = "LOST"
print "Received :  ", message

s.close()
