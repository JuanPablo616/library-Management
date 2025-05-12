📚 Sistema de Gestión de Biblioteca Comunitaria
Este es un sistema básico de gestión para una biblioteca comunitaria, desarrollado en Python. Permite agregar libros, registrar préstamos y devoluciones, eliminar libros del catálogo, listar por género y ver un resumen del inventario.

✅ Funcionalidades
Añadir libros – Agrega libros con título, autor, cantidad y género.

Buscar libros por título – Consulta los detalles de un libro ingresando su título.

Registrar préstamo de libro – Presta un libro si hay copias disponibles.

Devolver libro – Aumenta el número de copias disponibles al devolver un libro.

Eliminar libro del catálogo – Solo se puede eliminar si todas las copias están disponibles.

Listar libros por género – Muestra todos los libros disponibles de un género específico.

Resumen de inventario – Muestra el número total de títulos y de copias disponibles.

🎯 Géneros válidos
Fiction

Non Fiction

Science

Biography

Children

🚀 Cómo usar
Asegúrate de tener Python 3 instalado.

Ejecuta el programa con:

bash

python biblioteca.py
Puedes modificar el archivo para probar distintas funcionalidades o implementar un menú interactivo.

📥 Ejemplos de uso
Añadir un libro

Título: 1984  
Autor: George Orwell  
Copias: 5  
Género: Fiction
Buscar un libro

Buscar título: 1984  
Título: 1984  
Autor: George Orwell  
Género: Fiction  
Copias disponibles: 5
Prestar un libro

Prestar: 1984  
Préstamo registrado con éxito.
Devolver un libro

Devolver: 1984  
Libro devuelto con éxito.
Eliminar un libro

Eliminar: 1984  
Libro eliminado con éxito.
Género inválido

Género: Terror  
Error: 'Terror' no es un género válido.
Libro no encontrado

Buscar título: Desconocido  
Book not found.
📊 Resumen de inventario

--- Resumen de Inventario ---  
Total de títulos: 10  
Copias disponibles: 56
