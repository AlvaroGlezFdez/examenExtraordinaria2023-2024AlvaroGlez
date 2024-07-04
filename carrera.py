
from coche import Coches
class Carrera:
    def __init__(self):
        self.coches = []

    def agregar_coche(self, coche):
        self.coches.append(coche)

    def iniciar_carrera(self, duracion, intervalo):
        tiempo_actual = 0.0
        while tiempo_actual < duracion:
            for coche in self.coches:
                coche.mover(intervalo)
                print(f"{coche.nombre} - Posición: {coche.posicion:.1f}")
            tiempo_actual += intervalo

        # Determinar el ganador
        ganador = max(self.coches, key = lambda coche: coche.posicion)
        print(f"\nGanador: {ganador.nombre}")