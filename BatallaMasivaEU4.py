import random

general_atacante = 2
general_defensor = 1

ataque_unidad = 1
defensa_unidad = 2

terreno = 0

total_soldados_atacante = 1000
total_soldados_defensor = 1000
# Daño base de la unidad.
daño_roll = random.randint(0, 9)
print(f"Lanzamiento dado: {daño_roll}")
daño_base = daño_roll + max(0, general_atacante - general_defensor) + ataque_unidad - defensa_unidad - terreno

print(f"Daño base: {daño_base}")

# Multiplicador de daño

multiplicador = total_soldados_atacante / 1000 * ataque_unidad / 0.5 * (1 + 1) * (1 + 1) * (1 + 1 / 100)
print(f"Multiplicador: {multiplicador}")
