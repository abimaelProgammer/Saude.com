#!/usr/bin/env python

import cgitb, cgi
cgitb.enable(display=0, logdir="./")
form = cgi.FieldStorage()
circ = float(form.getvalue('var1'))
sexo = int(form.getvalue('var2'))


print("Content-type:text/html\n\n")
print("<html>")
print("""<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../voltar.css">
    <title>Resultado Cardiovascular</title>
</head>
<body>""")
print("<h1> RISCO DE DOENÇAS CARDIOVASCULARES  <h1>")
if sexo == 1 and circ >= 102 or sexo == 2 and circ >= 88:
    print("<h1> Risco: Altíssimo <h1>")
    print("<h1> Programas Recomendados: Redução de Peso <h1>")
elif sexo == 1 and circ >= 94 or sexo == 2 and circ >= 84:
    print("<h1> Risco: Alto <h1>")
    print("<h1> Programas Recomendados: Redução de Peso <h1>")
elif sexo == 1 and circ > 90 or sexo == 2 and circ > 80:
    print("<h1> Risco: Médio -> Programas Recomendados: Redução de Peso <h1>")

elif sexo == 1 and circ <= 90 or sexo == 2 and circ<= 80:
    print("<h1> Risco: Normal <h1>")
    print ("Programas Recomendados: Controle de Peso <h1>")
else:
    print("<h1> Digite um sexo válido <h1>")
#<!--menu -->
print("""<ul class="navbar">
 <li><a href="../index.html">MENU</a>
  <li><a href="../Circunferencia.html">SAÚDE CARDÍACA</a>
""")
print("</body>")
print("</html>")