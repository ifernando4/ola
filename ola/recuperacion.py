import sys,os,time
import mod

def menu():
    mod.nnmobre()
    mod.ndni()
    mod.nfondo()
    opciones()
def opciones():
    while(1):
        try:
            print("*****menu*****")
            print("1.- retiro")
            print("2.- tipo de cambio")
            print("3.- ahorro")
            print("4.-salir")
            print("elig una opcion")
            x=input()
            x=int(x)
            while(x<0 or x>4):
                print("escog una opcion vlid de 1  4")
                x=input()
                x=int(x)
            break
        except ValueError:
            print("error eliga una opcion valida")
    if(x==1):
        mod.nretiro()
        opciones()
    elif(x==2):
        print("esta opcion todavia no existe")
        opciones()
    elif(x==3):
        mod.nahorro()
        opciones()
    elif(x==4):
        sys.exit()
menu()