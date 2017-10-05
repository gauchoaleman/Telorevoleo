# coding: utf-8
import pilasengine
import selecciona_jugador

def iniciar_juego():
    print("iniciar juego")
    selecciona_jugador.selecciona_jugador(pilas,texto_menu,menuppal,FondoMenu)

def mostrar_ayuda():
    print("Ayuda")

def salir_del_juego():
    print("Tengo que salir...")
    sys.exit()

pilas = pilasengine.iniciar()

opcionesmenuppal= \
[
    ('iniciar juego', iniciar_juego),
    ('ayuda', mostrar_ayuda),
    ('salir', salir_del_juego),
]

menuppal = pilas.actores.Menu(opciones=opcionesmenuppal)
#menuppal.color=pilas.colores.Color(255,255,255,255)

print("band0")
pilas.fondos.Color(pilas.colores.negro)
FondoMenu = pilas.fondos.Fondo()
FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondo_menu.jpg')

print("band1")
texto_menu = pilas.actores.Texto("Telorevoleo")
print("band2")
texto_menu.y=200
texto_menu.color=pilas.colores.Color(255,0,0,0)
texto_menu.escala=[1,4.5]
texto_menu.rotacion=[0,360*3]

print("band3")
pilas.ejecutar()