#!/usr/bin/env python3
import os,json
print("Content-Type: text/html\r\n\r\n")
print
print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")


#Q1
print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
#print(json_object)

#Q2
for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        #print(f"<em>{param}</em> = {os.environ[param]}</li>")
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))


#Q3
for param in os.environ.keys():
    if (param == "HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
