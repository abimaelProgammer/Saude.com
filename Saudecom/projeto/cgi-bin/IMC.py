#!/usr/bin/env python

import cgitb, cgi
cgitb.enable(display=0, logdir="./")
form = cgi.FieldStorage()
altura = float(form.getvalue('var1'))
peso = float(form.getvalue('var2'))

print("Content-type:text/html\n\n")
print("<html>")
print("""<head>
    <meta charset="UTF-8">
        <link rel="stylesheet" href="../voltar.css">
    <title>IMC: Resultado</title>
</head>
<body>""")
print("<h1> ÍNDICE DE MASSA CORPORAL <h1>")
if altura < 0 or peso < 0:
    print("<h1> Digite um Peso e Altura maiores que 0 <h1>")
else:
    imc = peso / altura ** 2
    if imc > 40:
        print("<h1> IMC: %.2f Kg/m² => (Obesidade Grave) <h1>" % (imc))
    elif imc > 30:
        print("<h1> IMC: %.2f Kg/m² => (Obesidade) <h1>" % (imc))
    elif imc >= 25 and imc <= 29.9:
        print("<h1> IM"
              "C: %.2f Kg/m² => (Sobrepeso) <h1>" % (imc))
    elif imc >= 18.5 and imc <= 24.9:
        print("<h1> IMC: %.2f Kg/m² => (Normal) <h1>" % (imc))
    else:
        print("<h1> IMC: %.2f Kg/m² => (Abaixo do peso) <h1>" % (imc))
#<!--menu -->
print("""<ul class="navbar">
 <li><a href="../index.html">MENU</a>
  <li><a href="../IMC.html">IMC</a>""")
print("</body>")
print("</html>")