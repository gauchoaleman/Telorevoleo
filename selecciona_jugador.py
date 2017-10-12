# coding: utf-8
import pilasengine

#pilas = pilasengine.iniciar()

class Jugador(pilasengine.actores.Actor):
    nombre = "nombrejugador"

    def iniciar(self):
        print( "JUgador.iniciar")

def juegaRama(pilas):

    jugador=Jugador()
    print ("juegaRama")
    print(jugador.nombre)
    jugador.nombre="rama"
    print ("Rama jugadorlin42")

def juegaStefan():
    print ("juegaStefan")
    jugador = Jugador()
    jugador.nombre = "stefan"
#    jugador.probar()
#    jugador.formatear()

def juegaFede():
    print ("juegaFede")
    jugador = Jugador()
    jugador.nombre = "fede"
#    jugador.probar()
#    jugador.formatear()

def juegaNacho():
    print ("juegaNacho")
    jugador = Jugador()
    jugador.nombre = "nacho"
#    jugador.probar()
#   jugador.formatear()
###copiado de selecciona_jugador





def test():
    print( "hola test")

def selecciona_jugador(pilas):
    texto_actores = pilas.actores.Texto("Elegi tu jugador")
    texto_actores.y = 200
    texto_actores.color = pilas.colores.Color(255, 0, 0, 0)
    texto_actores.escala = 2
    menuJugadores(pilas)
    print ("En selecciona_jugador")

def menuJugadores(pilas):
    opciones = \
    [
        ('rama', juegaRama(pilas)),
        ('stefan', juegaStefan),
        ('fede', juegaFede),
        ('nacho', juegaNacho)
    ]
    menujugadores = pilas.actores.Menu(opciones=opciones)