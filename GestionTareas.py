


def mostrar_menu():
    print("\nSistema de Gestión de Tareas")
    print("----Agregar tarea (1)")
    print("----Eliminar tarea (2)")
    print("----Mostrar tareas(3)")
    print("----Salir(4)")



class Tarea: # Creacion de la clase Tarea con su constructor
    def __init__(self, titulo, descripcion=""):
        self.titulo = titulo
        self.descripcion = descripcion

    


class GestorDeTareas:
    def __init__(self):
        self.tareas = []  # creacion de la lista de tareas

    def agregar_tarea(self, titulo, descripcion=""):
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        print("Tarea añadida con éxito")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Tarea '{titulo}' eliminada con éxito.")
                return
        print(f"Tarea '{titulo}' no encontrada.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            for tarea in self.tareas:
                print(tarea)


def main():
    gestor = GestorDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea (opcional): ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == '2':
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
        elif opcion == '3':
            gestor.mostrar_tareas()
        elif opcion == '4':
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


if __name__ == "__main__":
    main()



