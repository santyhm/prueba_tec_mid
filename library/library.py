class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.prestado:
            print(f"Lo siento, el libro {libro} ya está prestado.")
        else:
            libro.prestado = True
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado el libro {libro}.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.prestado = False
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro {libro}.")
        else:
            print(f"{self.nombre} no tiene el libro {libro} en su posesión.")

    def __str__(self):
        return f"Miembro: {self.nombre}, Libros prestados: {[libro.titulo for libro in self.libros_prestados]}"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro {libro} ha sido agregado a la biblioteca.")

    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if not libro.prestado]
        if disponibles:
            print(f"Libros disponibles en la biblioteca {self.nombre}:")
            for libro in disponibles:
                print(f"- {libro}")
        else:
            print(f"No hay libros disponibles en la biblioteca {self.nombre}.")

    def __str__(self):
        return f"Biblioteca {self.nombre}, Libros totales: {len(self.libros)}"

if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0-14-015751-2")
    libro3 = Libro("La Odisea", "Homero", "978-0-14-026886-7")

    # Crear una biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Mostrar libros disponibles
    biblioteca.mostrar_libros_disponibles()

    # Crear un miembro
    miembro1 = Miembro("Juan Pérez")

    # Prestar libros a un miembro
    miembro1.prestar_libro(libro1)
    miembro1.prestar_libro(libro2)

    # Mostrar libros disponibles nuevamente
    biblioteca.mostrar_libros_disponibles()

    # Devolver un libro
    miembro1.devolver_libro(libro1)

    # Mostrar libros disponibles nuevamente
    biblioteca.mostrar_libros_disponibles()

    # Mostrar estado del miembro
    print(miembro1)
