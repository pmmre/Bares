# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bares.settings")

import django
django.setup()

from rango.models import Tapa,Bar


def populate():
    crear_tapa("Solomillo a la pimienta", "solomillo en su punto de pimienta","solomillo.jpg")
    crear_tapa("Pure", "calabazinos y apio","pure.jpg")
    crear_tapa("Ensalada cesar", "Ensalada con pollo y lechuga","ensalada.jpg")
    crear_tapa("Pollo agridulce", "Especialidad china","pollo.jpg")
    crear_tapa("Secreto iberico", "tapa para 2","secreto.jpg")

    create_bar('El ruisenior','Bar decorado al estilo bohemio','Calle Cañaveral, Granada')
    create_bar('La pocilga','Bar de barrio','Calle Gonzalo Gallas, Granada')
    create_bar('Tapeando','Bar con ambiente estudiantil','Las Gabias, Calle Pedro Antonio de Alarcon')

    add_tapa_a_bar('El ruisenior','Secreto iberico')
    add_tapa_a_bar('El ruisenior','Solomillo a la pimienta')
    add_tapa_a_bar('El ruisenior','Pollo agridulce')


    add_tapa_a_bar('La pocilga','Pure')
    add_tapa_a_bar('La pocilga','Ensalada cesar')

    add_tapa_a_bar('Tapeando','Secreto iberico')
    add_tapa_a_bar('Tapeando','Solomillo a la pimienta')
    add_tapa_a_bar('Tapeando','Pure')
    add_tapa_a_bar('Tapeando','Pollo agridulce')
    add_tapa_a_bar('Tapeando','Ensalada cesar')
def crear_tapa(name, des,img):
    p = Tapa.objects.get_or_create(nombre_tapa=name, descripcion=des,imagen="imagenes_tapa/"+img)
    return p

def create_bar(name,des,direc):
    c = Bar.objects.get_or_create(nombre_bar=name,slug=name,descripcion_bar=des,direccion=direc)
    return c

def add_tapa_a_bar(name,name2):
    bar = Bar.objects.get(nombre_bar=name)
    c = bar.tapas.add(Tapa.objects.get(nombre_tapa=name2))
    return c


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()