import random

# Ejercito atacante
general_atacante = 2
ataque_unidad = 1
total_soldados_atacante = 10000
disciplina_atacante = 1.0
habilidad_combate_atacante = 0.2
tactica_militar_atacante = 0.5
moral_atacante = 3


# Ejercito defensor
general_defensor = 1
defensa_unidad = 2
total_soldados_defensor = 1000
disciplina_defensor = 1.0
habilidad_combate_defensor = 0
tactica_militar_defensor = 0.5
moral_defensor = 3

terreno = 0



# Daño base de la unidad.
daño_roll = random.randint(0, 9)
print(f"Lanzamiento dado: {daño_roll}")
daño_base = daño_roll + max(0, general_atacante - general_defensor) + ataque_unidad - defensa_unidad - terreno

print(f"Daño base: {daño_base}")

# Multiplicador de daño

multiplicador = total_soldados_atacante / 10000 * 0.2 / tactica_militar_defensor * (1 + habilidad_combate_atacante) * (1 + disciplina_atacante) * (1 + 7 / 100)
print(f"Multiplicador: {multiplicador}")


# Bajas morales

bajas_morales = (15 + 5 * daño_base) * multiplicador * (1 + 0) * (1 + 0) * moral_atacante / 540 + (moral_defensor * 0.01)

print(f"Bajas morales: {bajas_morales}")

# Bajas de soldados

bajas = (15 + 5 * daño_base) * multiplicador * (1 + 0) * (1 + 0)
print(f"Bajas: {bajas}")
