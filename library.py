#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import bookClass as bc
import csv

def read(message):
    string = ""
    while not string:
            string = input(message)
    return string

class library():
    def __init__(self):
        self.data = []
    def add(self):
        author = read("Autor: ")
        title = read("Título: ") 
        editorial = read("Editorial: ")
        newBook = bc.book(len(self.data),author,title,editorial)
        self.data.append(newBook)
    def getBook(self, i):
        if i >= 0 and i < len(self.data):
            return self.data[i]
    def deleteBook(self, i):
        if i >= 0 and i < len(self.data):
            self.data.pop(i)
    def printList(self):
        valores = []
        for book in self.data:
            #print("Título: " + book.getTitle() + ". Autor: " + book.getAuthor() + ". Editorial: " + book.getEditorial() + ". Código: " + book.getCode())
            #print '{0:20%} {1:20%} {2:20%} {3:5%}'.format(book.getTitle(),book.getAuthor(),book.getEditorial(),book.getCode())
            print("{0:^10} {1:<30} {2:^40} {3:^20}".format(book.getCode(),book.getAuthor(),book.getTitle(),book.getEditorial()))

    def editBook(self, i, newAuthor, newTitle, newEditorial):
        if i >= 0 and i < len(self.data):
            if newAuthor:
                self.data[i].setAuthor(newAuthor)
            if newTitle:
                self.data[i].setTitle(newTitle)
            if newEditorial:
                self.data[i].setEditorial(newEditorial)
    def loadLibrary(self, filename):
        #raw_data = open(filename, 'rt')
        reader = csv.reader(open(filename,'rt'), delimiter=',',quoting=csv.QUOTE_NONE)
        data = list(reader)
        for book in data:
            newBook = bc.book(book[0],book[1],book[2],book[3])
            self.data.append(newBook)
    def writeLibrary(self,filename):
        if not filename:
            filename = 'data.csv'
        out = []
        for book in self.data:
            out.append((book.getCode(),book.getAuthor(),book.getTitle(),book.getEditorial()))
        with open(filename,'w') as f:
            writer = csv.writer(f)
            writer.writerows(out)
