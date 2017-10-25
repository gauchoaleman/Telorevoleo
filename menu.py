# coding: utf-8
import pilasengine
#import jugar

nombre = ''
def proybomba(proyectil, bomba):
    proyectil.eliminar()
    bomba.explotar()

def jugbomb(jugador, bomba):
    jugador.eliminar()
    print("Game over!")
    exit()

class Jugador(pilasengine.actores.Actor):
    def iniciar(self):
        global nombre
        self.imagen = "imagenes/"+nombre+".jpg"
        self.escala = 0.05


class Proyectil(pilasengine.actores.Actor):
    def iniciar(self):
        global nombre
        self.imagen = "imagenes/proyectil_"+nombre+".jpg"
        self.escala = 0.1

    def actualizar(self):
        self.rotacion += 12


class Cargar(pilasengine.escenas.Escena):

    def iniciar(self):
        #ArrancarJuego(nombre)
        pilas.actores.vincular(Proyectil)
        print("jugar1")
        pilas.actores.vincular(Jugador)
        print("jugar2")
        jugador = Jugador(pilas)
        print("jugar3")
        jugador.aprender("disparar",municion="Proyectil",angulo_salida_disparo=90)
        print("jugar4")
        jugador.aprender("moverseComoCoche")
        print("jugar5")
        bomba = pilas.actores.Bomba()
        bomba.x = -200
        bombas = pilas.actores.Grupo()
        bombas.agregar(bomba * 5)
        pilas.colisiones.agregar('proyectil', 'bomba', proybomba)
        pilas.colisiones.agregar('jugador', 'bomba', jugbomb)

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
                ('stefan', self.JuegaStefan),
                ('fede', self.JuegaFede),
                ('nacho', self.JuegaNacho),
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
        global nombre

        nombre="rama"
        pilas.escenas.vincular(Cargar)
        #pilas.escenas.vincular(Cargar(pilas))
        pilas.escenas.Cargar()
        pass

    def JuegaStefan(self):
        global nombre

        nombre="stefan"
        pilas.escenas.vincular(Cargar)
        #pilas.escenas.vincular(Cargar(pilas))
        pilas.escenas.Cargar()
        pass

    def JuegaFede(self):
        global nombre

        nombre="fede"
        pilas.escenas.vincular(Cargar)
        #pilas.escenas.vincular(Cargar(pilas))
        pilas.escenas.Cargar()
        pass

    def JuegaNacho(self):
        global nombre

        nombre="nacho"
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
