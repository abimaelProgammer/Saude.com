#!/usr/bin/env python

import cgitb, cgi
cgitb.enable(display=0, logdir="./")
form = cgi.FieldStorage()
altura = float(form.getvalue('var1'))
peso = float(form.getvalue('var2'))
circ = float(form.getvalue('var3'))
sexo = int(form.getvalue('var4'))

print("Content-type:text/html\n\n")
print("<html>")
print("""<head>
    <meta charset="UTF-8">
        <link rel="stylesheet" href="../voltar.css">
    <title>Resultado</title>
</head>
<body>""")
#IMC

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
        print("<h1> IMC: %.2f Kg/m² => (Sobrepeso) <h1>" % (imc))
    elif imc >= 18.5 and imc <= 24.9:
        print("<h1> IMC: %.2f Kg/m² => (Normal) <h1>" % (imc))
    else:
        print("<h1> IMC: %.2f Kg/m² => (Abaixo do peso) <h1>" % (imc))

#AGUA
print("<h1> QUANTIDADE NESCESSÁRIA DE ÁGUA <h1>")
agua = peso * 0.035
print("<h1> %.2f Litros por dia <h1>" % (agua))

#CIRCUNFERENCIA
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
  <li><a href="../checkup.html">CHECK-UP</a>""")
print("</body>")
print("</html>")