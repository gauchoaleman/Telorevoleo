import pilasengine


class MiActor(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/rama.jpg"

    def actualizar(self):
        self.rotacion += 2

pilas = pilasengine.iniciar()

pilas.actores.vincular(MiActor)
mi_actor = pilas.actores.MiActor()
mi_actor.x=0
mi_actor.y=0
pilas.ejecutar()