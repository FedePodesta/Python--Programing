import sys

print("Argumentos:", sys.argv, type(sys.argv))
for i in range(1,len(sys.argv)):
    print(f"Hola {sys.argv[i]}!")