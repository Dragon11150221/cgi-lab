#!/usr/bin/env python3
import cgi, cgitb
from secret import username,password
from get_data_from_form import secret_page,after_login_incorrect,login_page
form = cgi.FieldStorage()

current_username = form.getvalue('username')
current_password = form.getvalue('password')


print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<p><b>Username</b> %s <b>password</b> %s</p>" %(username,password))
print("</body>")
print("</html>")

if current_username == None or current_password == None:
    print(login_page())

elif current_username != username or current_password != password:
    print(after_login_incorrect())

else:
    print ("Set-Cookie:UserID = %s;\r\n"%username)
    print ("Set-Cookie: Password = %s;\r\n"%password)
    print(secret_page(current_username,current_password))
