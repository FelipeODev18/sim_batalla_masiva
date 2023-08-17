import random

class Regimiento:
    def __init__(self, nombre, disparo, choque, total_soldados, habilidad_combate, daño_disparo, daño_choque):
        self.nombre = nombre
        self.disparo = disparo
        self.choque = choque
        self.total_soldados = total_soldados
        self.habilidad_combate = habilidad_combate
        self.daño_disparo = daño_disparo
        self.daño_choque = daño_choque
        self.combatientes_restantes = total_soldados

    def disparar(self, objetivo):

