import shutil
import os

RTDISCO = ":/Aurora 0.5b - Release Package/Data/GameData"
RTCARATULAS = "C:/Users/SrTonyChop/Desktop/solido/Discos duros/caratulas"

Disco = input("Ingrese la letra donde esta montado el disco:")
Disco = Disco.upper()

ListCaraulas = os.listdir(RTCARATULAS)
ListDisco = os.listdir(Disco + RTDISCO)

for caratula in ListCaraulas:
    caratula = caratula.split(".")[0].split("GC")
    for datos in ListDisco:
        datos = datos.split("_")
        if caratula[1] == datos[0]:
            try:
                os.remove(Disco + RTDISCO + "/" +  datos[0] + "_" + datos[1] + "/GC" + datos[0] + ".asset")
                shutil.copy(RTCARATULAS + "/" + "GC" + caratula[1] + ".asset", Disco + RTDISCO + "/" +  datos[0] + "_" + datos[1] + "/GC" + datos[0] + ".asset")
            except:
                print("No hay prblema es el cod 2 de la usb o no encontro el GC de en alguna carpeta")
