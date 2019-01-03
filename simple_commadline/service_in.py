import traceback
import ole_dump as OLE
import ole_vba as VBA
from pdf_class_in import pdfClass
import json
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import sys
import time
import os


# please use lower case letters for more additions
bad_ext_list = {'exe', 'jar', 'apk', 'py', 'c', 'cpp', 'cs', 'html', 'js', 'sh', 'bat', 'dll'}
bad_magic_list = {'mz', '#i'}

def ProcessVBA(f_loc):
    data=VBA.GetInformation(f_loc)
    print(data)
    d_json = json.loads(data)
    is_malicious = 0
    if d_json['total'] == '0':
        return 0
    else:
        if d_json.get('AutoExec'):
            if d_json['AutoExec'] == d_json['total']:
                is_malicious = 0
                return is_malicious
            elif d_json['AutoExec'] != d_json['total']:
                if d_json.get('Suspicious'):
                    if d_json['Suspicious'] > '0':
                        is_malicious = 1
                        return is_malicious
                if d_json.get('IOC'):
                    if d_json['IOC'] > '0':
                        if d_json.get('Suspicious'):
                            if d_json['Suspicious'] > '0':
                                is_malicious = 1
                                return is_malicious
                        else:
                            is_malicious = 0
                            return is_malicious

        elif d_json.get('IOC'):
            if d_json['IOC'] > '0':
                if d_json.get('Suspicious'):
                    if d_json['Suspicious'] > '0' and d_json['total'] > '2':
                        is_malicious = 1
                        return is_malicious
                else:
                    is_malicious = 0
                    return is_malicious
        elif d_json.get('Suspicious'):
            if d_json['Suspicious'] > '0':
                is_malicious = 1
                return is_malicious
        elif d_json.get('Suspicious'):
            if d_json.get('IOC'):
                if d_json.get('AutoExec'):
                    is_malicious = 1
                    return is_malicious
        else:
            if d_json['total'] > '4':
                is_malicious = 1
                return is_malicious
    return is_malicious
def ProcessOLE(f_loc):

    global bad_magic_list
    global bad_ext_list
    
    ext_list = []
    magic_list = []
    
    is_malicious = 0
    is_ext_malicious=0
    is_magic_malicious = 0
    
    result = 0

    data=OLE.GetInformation(f_loc)
    print(data)
    if data.startswith('{"name"'):
        data_split = data.split(";")
        for d in data_split:
            d = d.decode('latin-1')
            d_json = json.loads(d)
            ext_list.append(d_json['ext'])
            magic_list.append(d_json['magic'])
        for ext in ext_list:
            if ext in bad_ext_list:
                is_ext_malicious = 1
                break
        for magic in magic_list:
            for bad_magic in bad_magic_list:
            	if magic.lower().startswith(bad_magic):
                	is_magic_malicious = 1
                	break
        if is_ext_malicious or is_magic_malicious:
            is_malicious = 1
        else:
            is_malicious = 0
        result = is_malicious
    else:
        result = 0
    return result

def ProcessPDF(f_loc):
    PDF = pdfClass()
    data = PDF.pdfScan(f_loc)
    if data > 0.70:
        is_malicious=0
    else:
        is_malicious=1
    result = is_malicious
    return result

def Main():
    #accepted file type
    #please use lower case letters
    accepted_vba = {'docm', 'doc', 'ppt', 'pptm', 'xls', 'xlsm'}
    accepted_ms = {'docx', 'docm', 'doc', 'pptx', 'ppt', 'pptm', 'xlsx', 'xls', 'xlsm'}
    accepted_pdf = {'pdf'}
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    print("Socket Initialized: Start sending data to 5005 Port using Socket")
    print("IMPORTANT: Please check client_sample.py for understanding")
    flag = True
    if flag == True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.settimeout(None)
        flag = False
    # this while loop in for request/replay process
    while flag == False:
        # receving smq msg from client and replacing it in argument array
        s.listen(1)
        conn, addr = s.accept()
        print('Connection address:', addr)
        while 1:
            try:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                print("received data:", data)
            #received = "C:\Users\Osama Chaudhary\Desktop\Data\DOCM.DOCM;DOCM"
                received = data
            except socket.error:
                conn, addr=s.accept()
                continue
            data_split = received.split(";")
            f_location=data_split[0]
            print(f_location)
            f_type=data_split[1].lower()

            is_malicious = 0
            ole_is_suspicious = 0
            vba_is_suspicious = 0
            pdf_is__suspicious = 0

            if f_type in accepted_ms:
                ole_is_suspicious=ProcessOLE(f_location)
                vba_is_suspicious = 0
                if f_type in accepted_vba:
                    vba_is_suspicious=ProcessVBA(f_location)
                if ole_is_suspicious or vba_is_suspicious:
                    is_malicious = 1
            if f_type in accepted_pdf:
                pdf_is__suspicious=ProcessPDF(f_location)
                is_malicious = pdf_is__suspicious
            print("Is_Malicious :"+str(is_malicious))
            try:
                conn.send(received+";"+str(is_malicious))
            except socket.error:
                conn, addr = s.accept()
                continue

# sc create nonpe binPath= "C:\Services\service_in.exe" DisplayName= "Non PE" start= auto
import os

if __name__ == '__main__':
    Main()
