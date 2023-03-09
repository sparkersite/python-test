valor1 = input("Valor 1:")
valor2 = input("Valor 2:")
if valor1 == valor2:
 print("valor1 y valor2 son iguales")
else:
 if valor1 > valor2:
  print("v1 es mayor que v2")
 else:
  print("v2 es mayor que v1")
i = 0
conca = ""
while i < int(valor1):
  conca = conca + "*"
  i += 1
print("Valor1: " + str(valor1) + " " + conca)
conca = ""
i = 0
while i < int(valor2):
  conca = conca + "*"
  i += 1
print("Valor2: " + str(valor2) + " " + conca)
archivonombre = input("Nombre del archivo: ")
archivonombre += ".txt"
print(archivonombre)
crearchivo = open(archivonombre, "a")
contenido = input("Contenido para el archivo: ")
crearchivo.write(contenido)
crearchivo.close()