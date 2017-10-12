import pilasengine
#import selecciona_jugador

class Jugador(pilasengine.actores.Actor):
    def iniciar(self):
        global jugador
        self.imagen = "imagenes/"+jugador.nombre+".jpg"
        self.escala = 0.1


class Proyectil(pilasengine.actores.Actor):
    def iniciar(self):
        global jugador
        self.imagen = "imagenes/proyectil_"+jugador.nombre+".jpg"


class Jugar(pilasengine.escenas.Escena):

    def iniciar(self,nombre):
        print ("A jugar "+nombre+"!!!")
        #pilas.actores.vincular(Proyectil)

        #jugador = Jugador(self,nombre)

        #jugador.aprender(self.habilidades.Disparar,
        #                 municion="Proyectil",
        #                 )

        #jugador.aprender("moverseComoCoche")
        pass

    def ejecutar(self):
        pass