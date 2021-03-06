# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

def proybomba(proyectil, bomba):
    proyectil.eliminar()
    bomba.explotar()

def jugbomb(jugador, bomba):
    jugador.eliminar()
    print("Game over!")
    exit()

def colisionajugbombas(jugador,bomba):
    jugador.eliminar()

class Jugador(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/rama.jpg"
        self.escala=0.05
        
class Proyectil(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/proyectil_rama.jpg"
        self.escala = 0.1

    def actualizar(self):
        self.rotacion += 12

pilas.actores.vincular(Proyectil)

jugador=Jugador(pilas)
proyectil = Proyectil(pilas)

jugador.aprender(pilas.habilidades.Disparar,
    municion="Proyectil",angulo_salida_disparo=90
    )

#jugador.radio_de_colision = 30
#proyectil.radio_de_colision = 10
jugador.aprender("moverseComoCoche")
jugador.aprender("LimitadoABordesDePantalla")

bomba = pilas.actores.Bomba()
bomba.x=-200
bombas = pilas.actores.Grupo()
bombas.agregar(bomba*5)
#pilas.colisiones.agregar(bomba,proyectil,colisionaproybombas)
pilas.colisiones.agregar('proyectil', 'bomba', proybomba)
pilas.colisiones.agregar('jugador', 'bomba', jugbomb)
#pilas.colisiones.agregar(jugador, bombas, colisionajugbombas)


#mi_grupo.aprender("moverseComoCoche")
pilas.ejecutar()