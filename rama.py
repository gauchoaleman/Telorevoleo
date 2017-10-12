# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()


class Jugador(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/rama.jpg"
        self.escala=0.1
        
class Proyectil(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/proyectil_rama.jpg"

pilas.actores.vincular(Proyectil)

jugador=Jugador(pilas)

jugador.aprender(pilas.habilidades.Disparar,
    municion="Proyectil",
    )

jugador.aprender("moverseComoCoche")

bomba = pilas.actores.Bomba()
mi_grupo = pilas.actores.Grupo()
mi_grupo.agregar(bomba*5)
mi_grupo.aprender("moverseComoCoche")
pilas.ejecutar()