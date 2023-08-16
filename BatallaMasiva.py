import random

class Unidades:
    def __init__(self, nombre, cantidad, disparo, choque, calidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.disparo = disparo
        self.choque = choque
        self.calidad = calidad

    def disparar(self):
        if self.disparo != 0:
            daño = (random.randint(1, 10) * self.disparo) * self.calidad
            print(f"{self.nombre} hizo daño: {daño}")
            return daño
        else:
            return 0

    def chocar(self):
        if self.choque != 0:
            daño = (random.randint(1, 10) * self.choque) * self.calidad
            return daño
        else:
            return 0

class Ejercito:
    def __init__(self, nombre, infanteria, caballeria, artilleria, tactica_militar, habilidad_general, disciplina, moral):
        self.nombre = nombre
        self.infanteria = infanteria
        self.caballeria = caballeria
        self.artilleria = artilleria
        self.tactica_militar = tactica_militar
        self.habilidad_general = habilidad_general
        self.disciplina = disciplina
        self.moral = moral
        self.total_cantidad = self.infanteria.cantidad + self.caballeria.cantidad + self.artilleria.cantidad

    def actualizar_cantidad(self):
        cantidad = self.infanteria.cantidad + self.caballeria.cantidad + self.artilleria.cantidad
        self.total_cantidad = cantidad
        print(f"{self.nombre} le quedan {self.total_cantidad} soldados")

    def fase_disparo(self, oponente):
        daño_infanteria = self.infanteria.disparar()
        daño_caballeria = self.caballeria.disparar()
        daño_artilleria = self.artilleria.disparar()

        daño_total = daño_artilleria + daño_caballeria + daño_infanteria
        print(f"daño total de las unidades: {daño_total}")

        daño_ejercito = daño_total * (self.habilidad_general + self.tactica_militar) * self.disciplina * self.moral
        print(f"daño total de {self.nombre}: {daño_ejercito}")

        daño_inflingido = daño_ejercito / oponente.disciplina
        print(f"daño inflingido: {daño_inflingido}")

        bajas_infanteria = daño_inflingido / oponente.infanteria.calidad
        print(f"bajas infanteria: {bajas_infanteria}")
        bajas_caballeria = daño_inflingido / oponente.caballeria.calidad
        print(f"bajas caballeria: {bajas_caballeria}")

        oponente.infanteria.cantidad -= daño_inflingido / oponente.infanteria.calidad
        oponente.caballeria.cantidad -= daño_inflingido / oponente.caballeria.calidad
        if oponente.artilleria.cantidad == 0:
            pass
        else:
            oponente.artilleria.cantidad -= daño_inflingido / oponente.artilleria.calidad
        oponente.actualizar_cantidad()

ejercito_uno = Ejercito(nombre="Ejercito Inglés", infanteria=Unidades(nombre="Infantería con Arco Largo", cantidad=4000, disparo=0.35, choque=0.20, calidad=1), caballeria=Unidades(nombre="Caballería Medieval", cantidad=1000, disparo=0, choque=0.45, calidad=2), artilleria=Unidades(nombre="Ninguna", cantidad=0, disparo=0, choque=0, calidad=0), tactica_militar=0.20, habilidad_general=1, disciplina=4, moral=3)
ejercito_dos = Ejercito(nombre="Ejercito Francés", infanteria=Unidades(nombre="Hombres de Armas", cantidad=4000, disparo=0.30, choque=0.35, calidad=1), caballeria=Unidades(nombre="Caballería Medieval", cantidad=1000, disparo=0, choque=0.45, calidad=2), artilleria=Unidades(nombre="Ninguna", cantidad=0, disparo=0, choque=0, calidad=0), tactica_militar=0.35, habilidad_general=1, disciplina=6, moral=5)



print(ejercito_uno.total_cantidad)
print(ejercito_dos.total_cantidad)
contador = 1
while ejercito_uno.total_cantidad > 0 and ejercito_dos.total_cantidad > 0:
    print(f"RONDA {contador}")
    ejercito_uno.fase_disparo(ejercito_dos)
    ejercito_dos.fase_disparo(ejercito_uno)
    contador += 1

print(ejercito_uno.total_cantidad)
print(ejercito_dos.total_cantidad)


