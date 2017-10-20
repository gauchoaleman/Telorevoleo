# coding: utf-8
import pilasengine
#import jugar

class Jugador(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagenpers = "imagenes/rama.jpg"
        self.escala = 0.1


class Proyectil(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagenproy = "imagenes/proyectil_rama.jpg"


class Cargar(pilasengine.escenas.Escena):

    def iniciar(self):
        #ArrancarJuego(nombre)
        pilas.actores.vincular(Proyectil)
        print("jugar1")
        pilas.actores.vincular(Jugador)
        print("jugar2")
        jugador = Jugador(pilas)

        proyectil = Proyectil(pilas)
        print("jugar3")
        #jugador.aprender(self.habilidades.Disparar,
        #                 municion="Proyectil",
        #                 )
        print("jugar4")
        jugador.aprender("moverseComoCoche")
        pass


    def ejecutar(self):
        pass


#class Jugador(pilasengine.actores.Actor):
    #nombre = "nombrejugador"

    #def iniciar(self):
    #    print( "JUgador.iniciar")

class SeleccionJugador(pilasengine.escenas.Escena):


    def iniciar(self):
        #pilas.fondos.Color(pilas.colores.negro)
        #FondoMenu = pilas.fondos.Fondo()
        #FondoMenu.imagen = pilas.imagenes.cargar('imagenes/maradona.jpg')
        texto_actores = pilas.actores.Texto("Elegi tu jugador")
        texto_actores.y = 200
        texto_actores.color = pilas.colores.Color(255, 0, 0, 0)
        texto_actores.escala = 2

        opcionesmenujugadores = \
            [
                ('rama', self.JuegaRama),
                ('stefan', self.QuienJuega),
                ('fede', self.QuienJuega),
                ('nacho', self.QuienJuega),
            ]

        menujugadores = pilas.actores.Menu(opciones=opcionesmenujugadores)

    def ejecutar(self):
        pass

    def QuienJuega(self):

        #jugador = Jugador(pilas)
        #jugador.nombre = nombre
        print "pasa en quienjuega"
        #print( "jugador.nombre: "+jugador.nombre)
        #pilas.escenas.vincular(Jugar)
        #pilas.escenas.Jugar(nombre)

        pass

    def JuegaRama(self):
        pilas.escenas.vincular(Cargar)
        #pilas.escenas.vincular(Cargar(pilas))
        pilas.escenas.Cargar()
        pass


class PantallaBienvenida(pilasengine.escenas.Escena):

    def iniciar(self):
        pilas.fondos.Color(pilas.colores.negro)
        FondoMenu = pilas.fondos.Fondo()
        FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondo_menu.jpg')
        texto_menu = pilas.actores.Texto("Telorevoleo")
        print("band2")
        texto_menu.y = 200
        texto_menu.color = pilas.colores.Color(255, 0, 0, 0)
        texto_menu.escala = [1, 4.5]
        texto_menu.rotacion = [0, 360 * 3]
        opcionesmenuppal = \
            [
                ('iniciar juego', iniciar_juego),
                ('ayuda', mostrar_ayuda),
                ('salir', salir_del_juego),
            ]

        menuppal = pilas.actores.Menu(opciones=opcionesmenuppal)
        pass

    def ejecutar(self):
        pass

def iniciar_juego():
    print("iniciar juego")
    pilas.escenas.vincular(SeleccionJugador)
    pilas.escenas.SeleccionJugador()


def mostrar_ayuda():
    print("Ayuda")

def salir_del_juego():
    print("Tengo que salir...")
    exit()

pilas = pilasengine.iniciar()


print("band0")
pilas.escenas.vincular(PantallaBienvenida)
pilas.escenas.PantallaBienvenida()
print("band3")
pilas.ejecutar()
