#!C:\Users\admin\AppData\Local\Programs\Python\Python310\python.exe

# Import CGI and CGIT module
import cgi, cgitb			

# to create instance of FieldStorage
# class which we can use to work
# with the submitted form data
form = cgi.FieldStorage()	
your_name = form.getvalue('your_name')	

# to get the data from fields
last_name = form.getvalue('last_name')

print("content-type: text/html\n\n" )
print ("<html>")
print ("<head>")
print ("<title>First CGI Program</title>")
print ("</head>")
print ("<body>")
if your_name=="onkar" and last_name == "nora":
    print ("<h2>Hello,  "+your_name+"  "+last_name+" </h2>" )
else:
    print ("<h2>Could not identify </h2>" )

print ("</body>")
print ("</html>")
