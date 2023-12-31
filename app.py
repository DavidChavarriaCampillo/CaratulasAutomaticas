import shutil
import os

# RTDISCO = ":/Aurora 0.5b - Release Package/Data/GameData"
RTDISCO = ":/Aurora/Data/GameData"
RTCARATULAS = "C:/Users/SrTonyChop/Desktop/GitHub/CaratulasAutomaticas/car"

Disco = input("Ingrese la letra donde esta montado el disco:")
Disco = Disco.upper()

ListCaraulas = os.listdir(RTCARATULAS)
ListDisco = os.listdir(Disco + RTDISCO)

for caratula in ListCaraulas:
    caratula = caratula.split(".")[0].split("GC")[1]
    for datos in ListDisco:
        datos = datos.split("_")
        if caratula == datos[0]:
            try:
                exist = os.path.exists(Disco + RTDISCO + "/" +  datos[0] + "_" + datos[1] + "/GC" + caratula + ".asset")
                if exist:
                    os.remove(Disco + RTDISCO + "/" +  datos[0] + "_" + datos[1] + "/GC" + caratula + ".asset")
                shutil.copy(RTCARATULAS + "/" + "GC" + caratula + ".asset", Disco + RTDISCO + "/" +  datos[0] + "_" + datos[1] )
            except:
                print("Fallo al remover o copiar el rchivo GC en el disco duro con juegos")

print('Caratulas instaladas con exito')