
import time

def ingreso_str(mensaje,error):
    dato = input(mensaje)
    while dato=="":
        print(error)
        dato = input(mensaje)
    return dato


def ingreso_int(mensaje,error):
    dato = input(mensaje)
    while True:
        try:
            dato = int(dato)
            break
        except ValueError:
            print(error)
        dato = input(mensaje)
    return dato


def ingreso_float(mensaje,error):
    dato = input(mensaje)
    while True:
        try:
            dato = float(dato)
            break
        except ValueError:
            print(error)
        dato = input(mensaje)
    return dato


def saludar(nombre):
    print("Hamburguesas IT")  
    print("Encargad@ -> " + nombre )
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :) ")


def ingresar():
    print("Bienvenido a Hamburguesas IT")
    nombre = ingreso_str("Ingrese su nombre encargad@: ","Error, campo vacio.")
    return nombre


def calcular(precios,pedido):
    total = 0
    total += pedido["ComboSimple"] * precios["ComboSimple"]
    total += pedido["ComboDoble"] * precios["ComboDoble"]  
    total += pedido["ComboTriple"] * precios["ComboTriple"]
    total += pedido["Flurby"] * precios["Flurby"]
    return total


def confirmar():
    respuesta = ingreso_str("¿Confirma el pedido? Y/N: ","Error. Campo vacio.")
    while respuesta.lower() != "y" and respuesta.lower() != "n" and respuesta.lower() != "yes" and respuesta.lower() != "no":
        print("Ingrese únicamente Y o N")
        respuesta = ingreso_str("¿Confirma el pedido? Y/N: ","Error. Campo vacio.")
    if respuesta == "y" or respuesta == "yes":
        return True
    else:
        return False


def guardarVentas(data):
    renglon = ""
    for n in data:
        if n == "total":
            renglon += str(data[n]) + "\n"
        else:
            renglon += str(data[n]) + ","
    f = open("ventas.txt","a")
    f.write(renglon)
    f.close()

def guardarEncargado(data):
    ingreso = "IN "+ data["ingreso"] +" Encargad@ "+ data["nombre"]+"\n"
    egreso = "OUT "+ data["egreso"] +" Encargad@ "+ data["nombre"] +" $ "+str(data["facturado"])+"\n"
    separador = ("#"*50)+"\n"
    f = open("registro.txt","a")
    f.write(ingreso)
    f.write(egreso)
    f.write(separador)
    f.close()


######################################################################


precios = {"ComboSimple":5,"ComboDoble":6,"ComboTriple":7,"Flurby":2}
salir = True

while salir:
    datosEncargado = {"nombre":"","ingreso":"","egreso":"","facturado":0}
    encargado = ingresar()
    inicio = time.asctime()
    datosEncargado["nombre"] = encargado
    datosEncargado["ingreso"] = inicio
    caja = 0
    print("\n"*2)
    while True:
        saludar(encargado)
        print("""
        1 – Ingreso de nuevo pedido
        2 – Cambio de turno
        3 – Apagar sistema
        """)
        opcion = ingreso_str(">>>","Error, ingreso vacio")
        if opcion == "1":
            print("\n"*2)
            pedido = {"cliente":"","fecha":"","ComboSimple":0,"ComboDoble":0,"ComboTriple":0,"Flurby":0,"total":0}
            pedido["cliente"] = ingreso_str("Ingrese el nombre del cliente: ","Error. No deje este campo vacio")
            pedido["ComboSimple"] = ingreso_int("Ingrese cantidad Combo S: ","Error, solo números")
            pedido["ComboDoble"] = ingreso_int("Ingrese cantidad Combo D: ","Error, solo números")
            pedido["ComboTriple"] = ingreso_int("Ingrese cantidad Combo T: ","Error, solo números")
            pedido["Flurby"] = ingreso_int("Ingrese cantidad Flurby: ","Error, solo números")
            costoTotal = calcular(precios,pedido)
            print("Total $", costoTotal)
            recibido = ingreso_float("Abona con $ ","Error, solo números")
            while costoTotal > recibido:
                print("Ingrese un monto mayor, no alcanza.")
                recibido = ingreso_float("Abona con $ ","Error, solo números")
            print("Vuelto $",recibido-costoTotal)
            estado = confirmar()
            if estado:
                caja += costoTotal
                pedido["fecha"] = time.asctime()
                pedido["total"] = costoTotal
                guardarVentas(pedido)
            else:
                print("Pedido cancelado")
        elif opcion == "2":
            datosEncargado["egreso"] = time.asctime()
            datosEncargado["facturado"] = caja
            guardarEncargado(datosEncargado)
            break
        elif opcion == "3":
            datosEncargado["egreso"] = time.asctime()
            datosEncargado["facturado"] = caja
            guardarEncargado(datosEncargado)
            print("¡Muchas gracias por usar nuestro programa!")
            salir = False
            break
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            print("\n*3")