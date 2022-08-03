try:
    int("a0")
except Exception as e:
    print("Ocurrió un error.",e.__class__)
else:
    print("todo salio bien")
finally:
    print("Final del bloque")