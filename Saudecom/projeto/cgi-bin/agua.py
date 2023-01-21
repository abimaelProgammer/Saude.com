#!/usr/bin/env python

import cgitb, cgi
cgitb.enable(display=0, logdir="./")
form = cgi.FieldStorage()
peso = float(form.getvalue('var1'))
print("Content-type:text/html\n\n")
print("<html>")
print("""<head>
    <meta charset="UTF-8">
     <link rel="stylesheet" href="../voltar.css">
    <title>Resultado Cardiovascular</title>
</head>
<body>""")

print("<h1>QUANTIDADE NESCESSÁRIA DE ÁGUA <h1><br>")
print("<h0.01> %.2f Litros por dia <h0.01><br>" % (peso * 0.035))
#<!--menu -->
print("""<ul class="navbar">
 <li><a href="../index.html">MENU</a>
  <li><a href="../agua.html">"BEBA ÁGUA!"</a>
""")

print("</body>")
print("</html>")