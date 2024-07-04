from coche import Coches
from carrera import Carrera

def main():
    # Crear coches (instancias)
    coche1 = Coches("Coche1", 150.0, 3.0)
    coche2 = Coches("Coche2", 140.0, 4.0)
    coche3 = Coches("Coche3", 160.0, 2.5)

    #carrera
    carrera = Carrera()
    carrera.agregar_coche(coche1)
    carrera.agregar_coche(coche2)
    carrera.agregar_coche(coche3)

    # Iniciar carrera
    duracion = 10.0  # Duración total de la carrera en segundos
    intervalo = 1.0  # Intervalo de tiempo en segundos
    carrera.iniciar_carrera(duracion, intervalo)

if __name__ == "__main__":
    main()