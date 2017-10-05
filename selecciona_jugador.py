# coding: utf-8
import pilasengine

class SeleccionarJugador(pilasengine.actores.Actor):
    nombre=""

    def cargardatos(self):
        self.imagen = "imagenes/"+self.nombre+".jpg"
        self.escala = 0.1
        self.aprender('LimitadoABordesDePantalla')
        self.aprender('SeMantieneEnPantalla')
        #self.aprender('RebotarComoPelota')


def selecciona_jugador(pilas,texto_menu,menuppal,FondoMenu):
    texto_menu.eliminar()
    menuppal.eliminar()
    FondoMenu.eliminar()
    texto_actores = pilas.actores.Texto("Elegi tu jugador")
    texto_actores.y = 200
    texto_actores.color = pilas.colores.Color(255, 0, 0, 0)
    texto_actores.escala = 2
    #mostrar_Jugadores(pilas)
    print ("En selecciona_jugador")
    JugadorRama = SeleccionarJugador(pilas)
    JugadorRama.nombre = "rama"
    print("JugadorRama.nombre: "+JugadorRama.nombre)
    JugadorRama.cargardatos()
    JugadorRama.imagen.x=50
    JugadorStefan = SeleccionarJugador(pilas)
    JugadorStefan.nombre = "stefan"
    JugadorStefan.cargardatos()
    JugadorFede = SeleccionarJugador(pilas)
    JugadorFede.nombre = "fede"
    JugadorFede.cargardatos()
    JugadorNacho = SeleccionarJugador(pilas)
    JugadorNacho.nombre = "nacho"
    JugadorNacho.cargardatos()

def mostrar_Jugadores(pilas):
    imagenRama = pilas.imagenes.cargar("imagenes/rama.jpg")
    actorRama = pilas.actores.Actor(imagenRama)
    imagenStefan = pilas.imagenes.cargar("imagenes/stefan.jpg")
    actorStefan = pilas.actores.Actor(imagenStefan)