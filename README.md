# Malicious Document Scanner (PDF and MS Office File)
Tool for detecting malicious MS Office and PDF files by in depth OLE and Macro analysis.
this tool is based on following repository
https://github.com/ozch/Malicious-Office-File-Detection-Using-Machine-Learning


# Required
- Python 2
first execute following commands in terminal
<code>pip install yara-python</code><br>
<code>pip install olefile</code><br>
<code>pip install oletools</code><br>
# Methodology
- this tool can be ran as a windows services (for linux machine usescommandline folder)
- check client_sample.py file to understand it's working
- service and client communicate at socket level.
- client only send the absolute path of file to the service using socket in return service reply with 1 or 0 (1 = Malicious,2 = Benign)
# Known Bugs
<emp> If there are any i don't know </emp>

