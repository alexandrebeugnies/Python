#coding:utf-8
import cgi
import http.cookies
import datetime
import os
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expriation.strftime("%a, %d-%b-%Y %H:%M:%S")

my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True
"""
expires
path
comment
domain
secure
version
httponly

Set-Cookie: pref_lang=fr; httponly
"""
print("Set-Cookie: pref_lang=fr; httponly")
print("Conten-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
	<meta charset="utf-8">
	<title>Ma page Web</title>
</head>
<body>
	<h1>Cookies avec Python</h1>
"""
print(html)
try:
	user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
	print("La langue choisie par l'utilisateur est :", user_lang["pref_lang"].value)
except(http.cookies.CookieError,KeyError):
	print("Non trouvé")
"""if "HTTP_COOKIE" in os.environ:
	print(os.environ.HTTP_COOKIE["HTTP_COOKIE"])
else:
	print("HTTP_COOKIE n'existe pas")


print("<p>Bonjour ! :)</p>")"""
html = """
</body>
</html>
"""

print(html)
