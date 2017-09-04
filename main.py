#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import library as lb



def start():
    print("Bienvenido al gestor de Bibliotecas 0.0.1")
    print("Los controles son los siguientes: ")
    print("(M) Muestra la lista de los libros que hay en la biblioteca.")
    print("(B) Borrar un libro.")
    print("(E) Editar un libro.")
    print("(A) Añadir un libro.")
    print("(Q) Salir del programa.")
    filename = input("Introduzca el nombre del archivo de datos: (Presione INTRO para la opción por defecto(data.csv))")
    if filename:
        biblioteca.loadLibrary(filename)
    else:
        biblioteca.loadLibrary('data.csv')


biblioteca = lb.library()
start()
option = lb.read("Introduzca una opción: ").upper()

while option != "Q":
    if option == "M":
        biblioteca.printList()
    elif option == "B":
        code = input("Introduce el código del libro para borrarlo: ")
        biblioteca.deleteBook(code)
    elif option == "E":
        code = input("Introduce el código del libro que quieres editar.")
        print("Introduzca \"\" si no quiere modificar ese campo.")
        author = input("Autor: ")
        title = input("Título: ")
        editorial = input("Editorial: ")
        biblioteca.editBook(code, author, title, editorial)
    elif option == "A":
        biblioteca.add()
    else:
        print("Opción no válida.")
    option = lb.read("Introduzca una opción: ").upper() 

print("Cerrando el programa.")
filename = lb.read("¿Dónde quieres guardar la biblioteca?(Presiona INTRO para la opción por defecto)")
biblioteca.writeLibrary(filename)