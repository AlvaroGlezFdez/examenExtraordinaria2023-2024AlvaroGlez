class Coches:
    def __init__(self, nombre, velocidad_maxima, aceleracion):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.posicion = 0.0
        self.velocidad = 0.0

    def mover(self, tiempo):
        # Actualizar la velocidad
        self.velocidad += self.aceleracion * tiempo
        if self.velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
        
        # Actualizar la posición
        self.posicion += self.velocidad * tiempo