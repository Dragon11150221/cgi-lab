#!/usr/bin/env python3
import os

print ("Set-Cookie:UserID = XYZ, Password = XYZ123;\r\n")
#print ("Set-Cookie:\r\n")

print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>COOKIES SET</title>")
print("</head>")
print("<body>")
print("<p>All done!</p>")
print("</body>")
print("</html>")

for param in os.environ.keys():
    if (param =="HTTP_COOKIE"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
