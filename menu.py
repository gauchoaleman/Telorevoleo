# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()
nombre = ''

class Cargar2(pilasengine.escenas.Escena):

    def iniciar(self):
        global enemigos
        global puntaje
        global puntaje2
        FondoMenu = pilas.fondos.Fondo()
        FondoMenu.imagen = pilas.imagenes.cargar('imagenes/fondonivel2.jpg')
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
            pilas.actores.Navemov()
        #bombamov.x = -200
        #bombasmov = pilas.actores.Grupo()
        print("jugar8")

        #bombasmov.agregar(bombamov * 5)

        print("jugar9")
        pilas.colisiones.agregar('proyectil', 'navemov', proynave)
        pilas.colisiones.agregar('jugador', 'navemov', jugnave)
        pass
        pilas.tareas.agregar(5, CargarNivel2)
        #texto_actores.color = pilas.colores.Color(255, 0, 0, 0)




def proybomba(proyectil, bombamov):
    global puntaje
    proyectil.eliminar()
    bombamov.explotar()
    bombamov = pilas.actores.Bombamov()
    print( "antes de aumentar puntaje")
    puntaje.aumentar(10)
    print("puntaje obtenido"+str(puntaje.obtener()))
    #texto_puntaje = pilas.actores.Texto(str(puntaje.obtener()))
    #texto_puntaje.y = 100
    #texto_puntaje.color = pilas.colores.amarillo
    #texto_puntaje.escala = 1

def jugbomb(jugador, bombamov):
    jugador.eliminar()
    pilas.escenas.PantallaBienvenida()

class Jugador(pilasengine.actores.Actor):
    nombre
    def iniciar(self):
        global nombre
        self.nombre = nombre
        self.imagen = "imagenes/"+nombre+".jpg"
        self.escala = 0.05


class Proyectil(pilasengine.actores.Actor):
    def iniciar(self):
        global nombre
        self.imagen = "imagenes/proyectil_"+nombre+".jpg"
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
        #bombamov.x = -200
        #bombasmov = pilas.actores.Grupo()
        print("jugar8")

        #bombasmov.agregar(bombamov * 5)

        print("jugar9")
        pilas.colisiones.agregar('proyectil', 'bombamov', proybomba)
        pilas.colisiones.agregar('jugador', 'bombamov', jugbomb)
        pass
        pilas.tareas.agregar(5, CargarNivel2)
        #texto_actores.color = pilas.colores.Color(255, 0, 0, 0)

    def ejecutar(self):
        pass

def CargarNivel2():
    pilas.escenas.Cargar2()

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
        pilas.fondos.Fondo("imagenes/pregunta.gif")
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
Nivel 2: Disparar naves.
El contacto con una nave o el disparo de una nave
finalizan el juego.
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
pilas.actores.vincular(Jugador)
pilas.escenas.vincular(Ayuda)
pilas.escenas.vincular(SeleccionJugador)
pilas.escenas.vincular(Cargar)
pilas.escenas.vincular(Cargar2)
pilas.actores.vincular(Bombamov)
pilas.escenas.vincular(PantallaBienvenida)
pilas.escenas.PantallaBienvenida()
print("band3")
pilas.ejecutar()
