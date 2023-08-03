#!/usr/bin/env python3
from gtts import gTTS
import os
from time import sleep
from colorama import init, Fore, Style, Back
init()
print(Style.BRIGHT+Fore.RED+"""
      ###############################
      #                                                                      #
      #      Author:      Hans Saldias                        #
      #      Creador:    Viernes 07 de julio              #  
      #      Uso :          Crear audio y guardarlo     #
      #      motivo:      Practica de programacion  #
      #      lenguaje:    python                                 #
      #                                                                      #
      #  #############################
""")

def sonido():
    print("""
                      #######################
                      ||  Crear audios personalizados  ||
                     #######################
                     
                            Created by: Hans Saldias
    """)
    if os.path.exists("audios_creados"):
        print("La carpeta audios_creados existe")
    else:
        os.mkdir("audios_creados") 
        print("carpeta Creada con exito!! ")
    while True:
        string = input("Ingrese el texto: ")
        gtts = gTTS(text = string, lang = "es")
        name = input("Ingrese nombre a poner al audio: ")
        gtts.save(f"audios_creados/{name}.mp3",)
        op = input("Desea crear otro ? (y/n) $  ")
        if op == "y":
                os.system("clear")
                sonido()
        else:
                print("Gracias por usar mi script .... ")
                break


try:
    while True:
        pw = input("Ingrese contraseña para uso $  ")  
        if pw == "user123":
            sonido()
        else:
            os.system("clear")
            print("Contraseña incorrecta\n")
            print("Contacte al creador: ")
except ValueError:
    print("Intente, nuevamente")
    