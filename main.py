#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import library as lb #Importamos el módulo donde he implementado la biblioteca('lb' para más comodidad.).

def showOptions():
    """
    Función auxiliar para hacer el código más legible.
    """
    print("Los controles son los siguientes: ")
    print("(M) Muestra la lista de los libros que hay en la biblioteca.")
    print("(D) Borrar un libro.")
    print("(E) Editar un libro.")
    print("(A) Añadir un libro.")
    print("(B) Buscar un libro por editorial o autor(sin tildes).")
    print("(O) Opciones disponibles.")
    print("(Q) Salir del programa.")


#Menú de inicio.
print("Bienvenido al Gestor de Bibliotecas.")
showOptions()



#Creamos un objeto 'library' y cargamos un archivo CSV con datos de libros.
biblioteca = lb.library()
filename = input("Introduzca el nombre del archivo de datos: (Presione INTRO para la opción por defecto(data.csv))")
if filename: 
    biblioteca.loadLibrary(filename)
else:
    biblioteca.loadLibrary('data.csv')


#Realizamos una lectura anticipada de la opción del menú.
option = lb.read("Introduzca una opción: ").upper() #La convertimos a mayúscula para evitar confusión entre minúsculas y mayúsculas.

#El menú lo he implementado con un 'while'(No comentaré nada aquí porque creo que se entiende bien). 
while option != "Q":
    if option == "M":
        biblioteca.printList()
    elif option == "D":
        code = lb.readCode("Introduce el código del libro para borrarlo: ")
        biblioteca.deleteBook(code)
    elif option == "E":
        code = lb.readCode("Introduce el código del libro que quieres editar.")
        print("Presione INTRO si no quiere modificar ese campo.")
        author = input("Autor: ")
        title = input("Título: ")
        editorial = input("Editorial: ")
        biblioteca.editBook(code, author, title, editorial)
    elif option == "A":
        biblioteca.add()
    elif option == "B":
        number = lb.readCode("Introduzca \"1\" si quiere buscar por autor, o \"2\" si quiere buscar por autor.")
        while number != 1 and number != 2: #Nos aseguramos de que la opción introducida sea 1 o 2.
            number = lb.readCode("Introduzca \"1\" si quiere buscar por autor, o \"2\" si quiere buscar por editorial.")
        name = lb.read("Introduzca el autor/editorial: ")
        biblioteca.search(number,name)
    elif option == "O":
        showOptions()
    else:
        print("Opción no válida.")
    option = lb.read("Introduzca una opción: ").upper() 


#Por último, cerramos el programa y guardamos los datos de la libreria en un archivo CSV.

print("Cerrando el programa.")
filename = input("¿Dónde quieres guardar la biblioteca?(Pulsa INTRO para la opción por defecto(data.csv))")
if filename: 
    biblioteca.writeLibrary(filename)
else:
    biblioteca.writeLibrary('data.csv')