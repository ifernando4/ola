import sys,os,time
def verificar(x):
    for c in x:
        if(ord(c)<65 or ord(c)>90)and (ord(c)<97 or ord(c)>122) and(ord(c)!=32):
            return False
    return True
def nnmobre():
    global nombre
    print("ingrese su nombre")
    nombre=input()
    while(not verificar(nombre)):
        print("ingrese correctamente su nombre")
        nombre=input()

def ndni():
    global dni
    global cambio
    dat_dni=""
    while(1):
        try:
            print("ingrese su dni")
            dni=input()
            dni=int(dni)
            while(len(str(dni))!=8):
                print("ingrese de tmaño 8")
                dni=input()
                dni=int(dni)
            data_dni=str(dni)
            break
        except ValueError:
            print("ingrese correctamente su dni")
    if(data_dni[0:2]=="30"):
        cambio=2
    elif(data_dni[0:2]=="29"):
        cambio=4
    elif(data_dni[0:2]=="28"):
        cambio=7
    else:
        print("debe ingresar un DNI que comiense con 29 30 28")
        ndni()
def nfondo():
    global fondo
    while(1):
        try:
            print("ingrese su fondo")
            fondo=input()
            fondo=int(fondo)
            while(fondo<0):
                print("ingrese correctamente")
                fondo=input()
                fondo=int(fondo)
            break
        except ValueError:
            print("ingrese correctamente")


def nretiro():
    global fondo
    print("CUENTA CON UN SALDO DE",fondo,"con un retiro de ")
    global retiro
    while(1):
        try:
            print("ingrese su monto de retiro")
            retiro=input()
            retiro=int(retiro)
            while(retiro<0):
                print("ingrese correctamente")
                retiro=input()
                retiro=int(retiro)
            break
        except ValueError:
            print("ingrese correctamente")
    fondo=fondo-retiro
    print("******banco scotiabank")
    print("NOMBRE            :",nombre)
    print("DNI               :",dni)
    print("Retiro    :",fondo)

def nahorro():
    global ahorro
    while(1):
        try:
            print("ingrese su ahorro")
            ahorro=input()
            ahorro=int(ahorro)
            while(ahorro<0):
                print("ingrese correctamente su ahorro")
                ahorro=input()
                ahorro=int(ahorro)
            break
        except ValueError:
            print("ingrese correctamente")
    nmeses()

def nmeses():
    global meses
    while(1):
        try:
            print("ingrese su cantidad de meses")
            meses=input()
            meses=int(meses)
            while(ahorro<0):
                print("ingrese correctamente su cantidad de meses")
                meses=input()
                meses=int(meses)
            break
        except ValueError:
            print("ingrese correctamente")
    iahorro()
def iahorro():
    ahorrot=ahorro+(ahorro*cambio/100*meses)
    mest=ahorrot/meses
    print("ahoroo total",ahorrot)
    print("horro mensual",mest)
