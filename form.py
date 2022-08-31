#coding:utf-8
import cgi
import cgitb

cgitb.enable()
form = cgi.fieldStorage()


html = """<!DOCTYPE html>
<head>
	<meta charset="utf-8">
	<title></title>
</head>
<body>
	<h1>Page Résultat</h1>
"""
print(html)
try:
	if form.getvalue("username"):
		username = form.getvalue("username")
		print(f"<p>Bonjour {username}</p> !")
		print("<script>alert('ok')</script>")
	else:
		raise Exception("Pseudo non transmis")
except:
	print("<p>Pseudo non transmis</p>")

html = """

</body>
</html>
"""

print(html)
