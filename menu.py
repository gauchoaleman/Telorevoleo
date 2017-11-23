# coding: utf-8
import random

import pilasengine
from pilasengine.actores import Moneda, Energia

pilas = pilasengine.iniciar()
nombre = ''
puntaje3=0
barra = pilas.actores.Energia(progreso=0, ancho=400, alto=25)

class Pinguino(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/pinguino.png"
    def actualizar(self):
        self.rotacion += 22

class Cargar3(pilasengine.escenas.Escena):

    def iniciar(self):
        print "ininiv3.1"
        global pilas
        global puntaje
        global puntaje2

        FondoMenu = pilas.fondos.Fondo()
        FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondonivel3.jpg')
        print("jugar3.1")
        print("jugar3.2")
        puntaje3 = pilas.actores.Puntaje(280, 220, color=pilas.colores.blanco, texto=puntaje2.obtener())
        jugador3 = Jugador(pilas)
        print("jugar3.3")
        jugador3.aprender("disparar",municion="Proyectil",angulo_salida_disparo=90)
        jugador3.aprender("LimitadoABordesDePantalla")

        print("jugar3.4")
        jugador3.aprender("moverseComoCoche")
        print("jugar3.5")

        print("jugar3.6")
        pilas.actores.Jefe()
        #bombamov.x = -200
        #bombasmov = pilas.actores.Grupo()
        print("jugar3.8")

        #bombasmov.agregar(bombamov * 5)

        print("jugar2.9")
        pilas.colisiones.agregar('proyectil', 'jefe', proyjefe)
        pilas.colisiones.agregar('jugador', 'jefe', jugjefe)
        pilas.colisiones.agregar('jugador', 'pinguino', jugpinguino)
        pass

impactosjefe=0
def proyjefe(proyectil, jefe):
    global barra
    global puntaje3
    global impactosjefe
    puntaje3 += 100
    impactosjefe +=1
    print "le dimos al jefe"

    barra.progreso += 10
    if impactosjefe >= 5:
        print( "**********Ganaste***********")
        pilas.escenas.PantallaBienvenida()


def jugjefe(jugador, navemov):
    jugador.eliminar()
    pilas.escenas.PantallaBienvenida()

def jugpinguino(jugador, navemov):
    jugador.eliminar()
    pilas.escenas.PantallaBienvenida()

class Jefe(pilasengine.actores.Actor):

    def iniciar(self):
        print("Jefe1")
        self.aprender("LimitadoABordesDePantalla")
        print("Jefe2")
        self.aprender("disparar",angulo_salida_disparo=90,control=None,municion=Proyectil)
        self.aprender("puedeexplotar")
        print("Jefe3")
        self.aprender("LimitadoABordesDePantalla")
        self.escala = 0.4
        #self.aprender("PuedeExplotar")
        self.imagen = 'imagenes/jefe.png'
        self.tarea_disparar= pilas.tareas.siempre(0.5,self.realizar_disparo)

        self.x = 320
        self.y = 0

        pass

    #def explotar(self):
    #    #TODO agregar explosión
    #    print ("Bum")
    #    self.eliminar()

    def realizar_disparo(self):
        self.aprender("disparar", control=None, municion='Pinguino',
                      angulo_salida_disparo=pilas.azar(250, 290))  # , frecuencia_de_disparo =1)
        self.disparar()
        return True

    #pilas.tareas.agregar(1, dispara)

    def actualizar(self):
        self.x += pilas.azar(-17,17)
        self.y += pilas.azar(-17,17)
        self.rotacion = (pilas.azar(-180,+180))
        #[0, 360 * 3]


class BalaNivel2(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/balanivel2.png"

class Cargar2(pilasengine.escenas.Escena):

    def iniciar(self):
        global pilas
        global enemigos
        global puntaje
        global puntaje2
        FondoMenu = pilas.fondos.Fondo()
        FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondonivel2.jpg')
        print("jugar2.1")
        print("jugar2.2")
        puntaje2 = pilas.actores.Puntaje(280, 220, color=pilas.colores.blanco, texto=puntaje.obtener())
        jugador2 = Jugador(pilas)
        print("jugar2.3")
        jugador2.aprender("disparar",municion="Proyectil",angulo_salida_disparo=90)
        jugador2.aprender("LimitadoABordesDePantalla")

        print("jugar2.4")
        jugador2.aprender("moverseComoCoche")
        print("jugar2.5")

        print("jugar2.6")
        x = 0
        for x in range(1, 6):
            pilas.actores.Navemov()
            pilas.actores.Monedarev()
        #bombamov.x = -200
        #bombasmov = pilas.actores.Grupo()
        print("jugar2.8")

        #bombasmov.agregar(bombamov * 5)

        print("jugar2.9")
        pilas.colisiones.agregar('proyectil', 'navemov', proynave)
        pilas.colisiones.agregar('jugador', 'navemov', jugnave)
        pilas.colisiones.agregar('jugador', 'balanivel2', jugproynave)
        pilas.colisiones.agregar('monedarev', 'jugador', monedajugador2)
        pass



class Navemov(pilasengine.actores.Actor):

    def iniciar(self):
        print("Navemov1")
        self.aprender("LimitadoABordesDePantalla")
        print("Navemov2")
        self.aprender("disparar",angulo_salida_disparo=90,control=None)
        self.aprender("puedeexplotar")
        self.fuentenave = pilas.azar(1,4)
        print("Navemov3")
        self.aprender("LimitadoABordesDePantalla")
        self.escala = 0.05
        self.aprender("PuedeExplotar")
        self.imagen = 'imagenes/nave.png'
        self.tarea_disparar= pilas.tareas.siempre(2,self.realizar_disparo)

        #print("fuentebomba"+self.fuentebomba)

        if( self.fuentenave==1):
            self.x = 320
            self.y = 0
        if (self.fuentenave == 2):
            self.x = 0
            self.y = 240
        if (self.fuentenave == 3):
            self.x = -320
            self.y = 0
        if (self.fuentenave == 4):
            self.x = 0
            self.y = -240
        pass

    #def explotar(self):
    #    #TODO agregar explosión
    #    print ("Bum")
    #    self.eliminar()

    def realizar_disparo(self):
        self.aprender("disparar", control=None, municion='BalaNivel2',
                      angulo_salida_disparo=pilas.azar(250, 290))  # , frecuencia_de_disparo =1)
        self.disparar()
        return True

    #pilas.tareas.agregar(1, dispara)

    def actualizar(self):
        self.x += pilas.azar(-17,17)
        self.y += pilas.azar(-17,17)
        self.rotacion = (pilas.azar(-180,+180))
        #[0, 360 * 3]

def jugproynave(jugador, proyectilnave):
    jugador.eliminar()
    pilas.escenas.PantallaBienvenida()

def jugnave(jugador, navemov):
    jugador.eliminar()
    pilas.escenas.PantallaBienvenida()

def proynave(proyectil, navemov):
    global puntaje2
    proyectil.eliminar()
    navemov.eliminar()
    #navemov.explotar()
    #explosion = pilas.actores.explosion.Explosion(x=navemov.x,y=navemov.y)
    navemov = pilas.actores.Navemov()
    print( "antes de aumentar puntaje")
    puntaje2.aumentar(10)
    print("puntaje obtenido"+str(puntaje2.obtener()))

monedascomidas2 = 0
def monedajugador2(moneda,jugador):
    global puntaje2
    global monedascomidas2
    moneda.eliminar()
    puntaje2.aumentar(50)
    monedascomidas2 +=1
    if monedascomidas2 >= 1:
        monedascomidas2 = 0
        CargarNivel3()

monedascomidas1 = 0
def monedajugador(moneda,jugador):
    global puntaje
    global monedascomidas1
    moneda.eliminar()
    puntaje.aumentar(50)
    monedascomidas1 +=1
    if monedascomidas1 >= 1:
        monedascomidas1 = 0
        CargarNivel2()

def proybomba(proyectil, bombamov):
    global puntaje
    proyectil.eliminar()
    bombamov.explotar()
    bombamov = pilas.actores.Bombamov()
    print( "antes de aumentar puntaje")
    puntaje.aumentar(10)
    print("puntaje obtenido"+str(puntaje.obtener()))

def jugbomb(jugador, bombamov):
    bombamov.explotar()
    jugador.eliminar()
    pilas.escenas.PantallaBienvenida()

class Jugador(pilasengine.actores.Actor):
    nombre
    def iniciar(self):
        global nombre
        self.nombre = nombre
        self.imagen = "imagenes/"+nombre+".png"
        self.escala = 0.05


class Proyectil(pilasengine.actores.Actor):
    def iniciar(self):
        global nombre
        self.imagen = "imagenes/proyectil_"+nombre+".png"
        self.escala = 0.1

    def actualizar(self):
        self.rotacion += 12

class Bombamov(pilasengine.actores.Bomba):

    def iniciar(self):
        self.aprender("LimitadoABordesDePantalla")
        self.fuentebomba = pilas.azar(1,4)
        #print("fuentebomba"+self.fuentebomba)

        if( self.fuentebomba==1):
            self.x = 320
            self.y = 0
        if (self.fuentebomba == 2):
            self.x = 0
            self.y = 240
        if (self.fuentebomba == 3):
            self.x = -320
            self.y = 0
        if (self.fuentebomba == 4):
            self.x = 0
            self.y = -240
        pass
    def actualizar(self):
        self.x += pilas.azar(-17,17)
        self.y += pilas.azar(-17,17)

class Monedarev(pilasengine.actores.Actor):

    def iniciar(self):
        self.aprender("LimitadoABordesDePantalla");
        self.imagen = 'imagenes/moneda.png'
        self.escala = 0.2
        self.x= random.randint(-320, 320)
        self.y = random.randint(-240, 240)

    def actualizar(self):
        self.rotacion += 10

class Cargar(pilasengine.escenas.Escena):

    def iniciar(self):
        global enemigos
        global puntaje
        puntaje = pilas.actores.Puntaje(280, 220, color=pilas.colores.blanco,texto=0)
        FondoMenu = pilas.fondos.Fondo()
        FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondonivel1.jpg')

        print("jugar1")

        print("jugar2")
        jugador = Jugador(pilas)
        print("jugar3")
        jugador.aprender("disparar",municion="Proyectil",angulo_salida_disparo=90)
        jugador.aprender("LimitadoABordesDePantalla")

        print("jugar4")
        jugador.aprender("moverseComoCoche")
        print("jugar5")

        x=0
        for x in range (1,6):
            pilas.actores.Bombamov()
            pilas.actores.Monedarev()
        #bombamov.x = -200
        #monedas = pilas.actores.Grupo()
        print("jugar8")

        #monedas.agregar(monedas * 5)

        print("jugar9")
        pilas.colisiones.agregar('proyectil', 'bombamov', proybomba)
        pilas.colisiones.agregar('jugador', 'bombamov', jugbomb)
        pilas.colisiones.agregar('monedarev', 'jugador', monedajugador)
        #pilas.tareas.agregar(5, CargarNivel2)
        #texto_actores.color = pilas.colores.Color(255, 0, 0, 0)

    def ejecutar(self):
        pass

def CargarNivel2():
    pilas.escenas.Cargar2()

def CargarNivel3():
    print "por cargar nivel3"
    pilas.escenas.Cargar3()

class SeleccionJugador(pilasengine.escenas.Escena):
    def iniciar(self):
        FondoMenu = pilas.fondos.Fondo()
        FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondo_seljug.jpg')
        texto_actores = pilas.actores.Texto("Elegi tu jugador")
        texto_actores.y = 100
        texto_actores.color = pilas.colores.Color(255, 0, 0, 0)
        texto_actores.escala = 2

        opcionesmenujugadores = \
            [
                ('rama', self.JuegaRama),
                ('stefan', self.JuegaStefan),
                ('fede', self.JuegaFede),
                ('nacho', self.JuegaNacho),
                ('facu', self.JuegaFacu),
            ]

        menujugadores = pilas.actores.Menu(opciones=opcionesmenujugadores)

    def ejecutar(self):
        pass

    def JuegaRama(self):
        global nombre

        nombre="rama"
        pilas.escenas.Cargar()
        pass

    def JuegaStefan(self):
        global nombre

        nombre="stefan"
        pilas.escenas.Cargar()
        pass

    def JuegaFede(self):
        global nombre

        nombre="fede"
        pilas.escenas.Cargar()
        pass

    def JuegaNacho(self):
        global nombre

        nombre="nacho"
        pilas.escenas.Cargar()
        pass

    def JuegaFacu(self):
        global nombre

        nombre="facu"
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
        texto_trucho = pilas.actores.Texto("Un Juego Trucho")
        texto_trucho.aprender("LimitadoABordesDePantalla")
        texto_trucho.aprender("RebotarComoPelota")
        texto_trucho.y = 150
        texto_trucho.color = pilas.colores.Color(0, 0,255,255)
        texto_trucho.escala = 3
        opcionesmenuppal = \
            [
                ('iniciar juego', iniciar_juego),
                ('ayuda', mostrar_ayuda),
                ('salir', salir_del_juego),
            ]

        menuppal = pilas.actores.Menu(opciones=opcionesmenuppal,color_normal=pilasengine.colores.amarillo, color_resaltado=pilasengine.colores.blanco)

        pass

    def ejecutar(self):
        pass

class Ayuda(pilasengine.escenas.Escena):

    def iniciar(self):
        pilas.fondos.Fondo("imagenes/pregunta.jpg")
        self.crear_texto_ayuda()
        self.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)
        pass

    def crear_texto_ayuda(self):
        self.pilas.actores.Texto("AYUDA", y=200)
        self.pilas.actores.Texto(MENSAJE_AYUDA)
        #self.pilas.actores.Texto.color = pilas.colores.Color(0, 0, 0, 0)
        self.pilas.avisar("Pulsa ESC para regresar")

    def cuando_pulsa_tecla(self, *k, **kw):
        pilas.escenas.PantallaBienvenida()

    def ejecutar(self):
        pass

MENSAJE_AYUDA = """
El jugador se mueve con las flechas y 
dispara presionando espacio.
Nivel 1: Disparar los proyectiles bajando bombas. 
El contacto con una bomba finaliza el juego  
Para pasar de nivel hay que juntar las monedas
Nivel 2: Disparar naves.
El contacto con una nave o el disparo de una nave
finalizan el juego.
Para pasar de nivel hay que juntar las monedas
Nivel 3: Sorpresa.
"""

def iniciar_juego():
    print("iniciar juego")

    pilas.escenas.SeleccionJugador()


def mostrar_ayuda():

    pilas.escenas.Ayuda()

    print("Ayuda")

def salir_del_juego():
    print("Tengo que salir...")
    exit()




#puntaje.z = -10
pilas.actores.vincular(Proyectil)
pilas.actores.vincular(BalaNivel2)
pilas.actores.vincular(Pinguino)
pilas.actores.vincular(Jugador)
#pilas.actores.vincular(Energia)
pilas.escenas.vincular(Ayuda)
pilas.escenas.vincular(SeleccionJugador)
pilas.escenas.vincular(Cargar)
pilas.escenas.vincular(Cargar2)
pilas.escenas.vincular(Cargar3)
pilas.actores.vincular(Jefe)
pilas.actores.vincular(Bombamov)
pilas.actores.vincular(Navemov)
pilas.actores.vincular(Monedarev)
pilas.escenas.vincular(PantallaBienvenida)
pilas.escenas.PantallaBienvenida()
print("band3")
pilas.ejecutar()
