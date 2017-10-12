# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
pilas.fondos.Color(pilas.colores.negro)
FondoMenu = pilas.fondos.Fondo()
FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondo_menu.jpg')


texto = pilas.actores.Texto("Telorevoleo")
texto.y=200
texto.color=pilas.colores.Color(255,0,0,0)
texto.escala=[1,4.5]
texto.rotacion=[0,360]
pilas.ejecutar()
