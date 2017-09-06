#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import csv

def read(message):
    """
    Función auxiliar que lee un str y se asegura de que no sea un string vacío.
    :param message: Mensaje que aparecerá al pedir que se introduzca el dato.
    :return: string (no vacío)
    """
    string = ""
    while not string:
            string = input(message)
    return string

def readCode(message):
    """
    Función auxiliar que lee un int y se asegura de que el dato introducido sea un int(positivo estricto).
    :param message: Mensaje que aparecerá al pedir que se introduzca el dato.
    :return: int (>0)
    """
    number = 0
    while number <= 0:
        try:
            number = int(input(message))
            return number
        except:
            #Le asigno un valor no válido (0, porque el 'code' de un objeto 'book' siempre es positivo estricto).
            print("Error: debe introducir un número positivo estricto.")
            number = 0

class book():
    """
    Representa un libro con: autor, título, editorial y un código identificativo(positivo estricto).
    """
    def __init__(self, code, author, title, editorial):
        """
        Crea un nuevo objeto 'book'.
        :param author: Autor del libro.
        :param title: Título del libro.
        :param editorial: Editorial del libro.
        :param codigo: Código identificativo del libro (positivo estricto). 
        """
        self.author = author
        self.title = title
        self.editorial = editorial
        self.code = code


class library():
    """
    Alberga una colección de libros en un array (data) formado por objetos 'book'.
    """
    def __init__(self):
        """
        Construye un objeto 'library' e inicializa una lista (data) donde se guardarán los libros ('book')  de la biblioteca.
        """
        self.data = []
    def add(self):
        """
        Añade un nuevo objeto 'book' a la lista de libros.
        :return: Void.
        """
        author = read("Autor: ")
        title = read("Título: ") 
        editorial = read("Editorial: ")
        #'int(self.data[len(self.data)-1].code)+1' da como resultado el 'code' del último
        #libro de 'data' y le suma uno, asegurando así que ningún libro tenga un 'code' igual.
        #Lo convierto a 'int' porque al cargar los datos con 'loadLibrary()' el 'code' se 
        #guarda como un string.
        newBook = book(int(self.data[len(self.data)-1].code)+1,author.upper(),title.upper(),editorial.upper()) #Lo paso a mayuscula para evitar errores de búsqueda con las minúsculas/mayúsculas.
        if self.isRepeated(newBook):
            print("Error: El libro quiere añadir ya se encuentra en la biblioteca.")
        else:
            self.data.append(newBook)
            print("Libro añadido correctamente.")
    def isRepeated(self, bk):
        """
        Comprueba si un libro está ya en la biblioteca.
        :param bk: objeto 'bk'.
        :return: True si el libo 'bk' está en la biblioteca, False, en caso contrario.
        """
        equal = False
        for Book in self.data:
            #He considerado que libros con mismo autor y mismo título, pero diferente EDITORIAL son libros distintos.
            if bk.author == Book.author and bk.title == Book.title and bk.editorial == Book.editorial:
                equal = True
                break
        return equal

    def deleteBook(self, i):
        """
        Borra el libro con código 'i'.
        Si no encuentra dicho libro, aparece un mensaje de error (el cual se encuentra en el método 'searchBookPos()')
        :param i: Código del libro.
        :return: Void.
        """
        if i > 0:
            if self.searchBookPos(i) != -1:
                self.data.pop(self.searchBookPos(i))
                print("Libro borrado correctamente.")
    def printList(self):
        """
        Muestra la lista de libros en la biblioteca.
        :return: Void.
        """
        print("{0:^20} {1:^30} {2:^50} {3:<20}".format("CODIGO","AUTOR","TITULO","EDITORIAL"))
        print("")
        for bk in self.data:
            print("{0:^20} {1:<30} {2:^50} {3:<20}".format(bk.code,bk.author,bk.title,bk.editorial))

    def editBook(self, i, newAuthor, newTitle, newEditorial):
        """
        Borra el libro con código 'i'.
        Si no encuentra dicho libro, aparece un mensaje de error (el cual se encuentra en el método 'searchBookPos()'.
        Si alguno de los 3 últimos argumentos es '', ese campo no se edita.
        :param newAuthor: Nuevo autor del libro.
        :param newTitle: Nuevo título del libro.
        :param newEditorial: Nueva editorial del libro.
        :return: Void.
        """
        if i > 0:
            #Asignamos el valor de 'searchBookPos(i)' a una variable ('index') para no tener que buscar el mismo libro 3 veces.
            index = self.searchBookPos(i)
            if index != -1: #searchBookPos devuelve '-1' si el libro no se encuentra en la biblioteca.
                #Hacemos una copia del libro a editar, para evitar que al almacenar el libro editado, este esté repetido.
                candidate = book(self.data[index].code,self.data[index].author,self.data[index].title,self.data[index].editorial)
                if newAuthor:
                    candidate.author = newAuthor.upper()
                if newTitle:
                    candidate.title = newTitle.upper()
                if newEditorial:
                    candidate.editorial = newEditorial.upper()
                if not self.isRepeated(candidate): #Solo añadimos el libro editado si después de la edición no está repetido.
                    self.data[index] = candidate
                else:
                    print("Error: Ya hay un libro con esas características en la biblioteca.")
    def searchBookPos(self, i):
        """
        Busca la posición de un objeto 'book' en 'data' a partir del código de 'book'.
        Si no encuentra dicho libro, aparece un mensaje de error (el cual se encuentra en el método 'searchBookPos()'.
        :param i: Código del libro.
        :return: Posición en 'data' de 'book' con código 'i'.
        """
        index = 0
        for bk in self.data:                      
            if i == int(bk.code): #Lo convierto a 'int' porque al cargar los datos con 'loadLibrary()' el 'code' se guarda como un string.
                return index
            else:
                index+=1
        else:
            print("No hay ningún libro asociado a ese código en esta biblioteca.")
            return -1 #Devuelvo '-1' si no existe 'book' con código 'i' en 'data'.(En la implementación de la librería he considerado el '-1' no válido, aunque sí lo sea en python.) 

    def search(self, arg, name):
        """
        Busca libros en la biblioteca por autor/editorial.
        :param arg: Si vale, 1 busca por autor. Si vale 2, busca por editorial.
        :param name: nombre del autor/editorial por el que se desea buscar.
        :return: Void.
        """
        if arg == 1:
            for bk in self.data:
                if bk.author == name.upper():
                    print("{0:^10} {1:<30} {2:^40} {3:^20}".format(bk.code,bk.author,bk.title,bk.editorial))
        if arg == 2:
            for bk in self.data:
                if bk.editorial == name.upper():
                    print("{0:^10} {1:<30} {2:^40} {3:^20}".format(bk.code,bk.author,bk.title,bk.editorial))
    def loadLibrary(self, filename):
        """
        Carga los datos de una biblioteca (objeto 'library') a partir de un arhivo CSV.
        :param filename: Nombre del archivo CSV.
        """
        reader = csv.reader(open(filename,'rt'), delimiter=',',quoting=csv.QUOTE_NONE)
        #Convertimos 'reader' para facilitar la carga de la biblioteca.
        data = list(reader)
        #Usamos el constructor de la clase 'book' para crear los libros y añadirlos a 'data'.
        for bk in data:
            newBook = book(bk[0],bk[1],bk[2],bk[3]) #El formato de cada fila en el CSV es ('code','author','title','editorial').
            self.data.append(newBook)
    def writeLibrary(self,filename):
        """
        Escribe los datos de una biblioteca (objeto 'library') en un arhivo CSV.
        :param filename: Nombre del archivo CSV.
        """
        #Creamos una lista, en la cual cada item esta formado por ('code','author','title','editorial') del libro correspondiente.
        #Esto lo hacemos porque a 'writer.writerows()' hay que pasarle una lista con estas condiciones para escribir correctamente el archivo CSV.
        out = []
        for bk in self.data:
            out.append((bk.code,bk.author,bk.title,bk.editorial))
        with open(filename,'w') as f:
            writer = csv.writer(f)
            writer.writerows(out)
