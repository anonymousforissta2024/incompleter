#Source: https://stackoverflow.com/questions/24950570/typeerror-cant-convert-int-object-to-str-implicitly-python
import cgi
form = cgi.FieldStorage()

name = str(form.getvalue("name"))
age = int(form.getvalue("age"))

print ("""Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html><head>
<title>Lab 9</title>
</head><body>
""")

print ("<p>Hello," +name+ ".</p>")
print ("Next year you will be" + str(age+1) + "years old")
print ("</body></html>") 