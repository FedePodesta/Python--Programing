# with open("file.txt", "r" ) as f:
#     for line in f:
#         print("línea", line)


# with open("file.txt", "r" ) as f:
#     texto = f.read()
#     print(texto)

n = 1
with open("file.txt", "r" ) as f:
    f1 = open("salida.txt", "w")
    for line in f:
        cadena = "Línea" + str(n) + line
        f1.write(cadena)
        n+=1
    f1.close()