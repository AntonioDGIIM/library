#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

class book():
    def __init__(self, code, author, title, editorial):
        self.author = author
        self.title = title
        self.editorial = editorial
        self.code = code
    def getAuthor(self):
        return self.author
    def getTitle(self):
        return self.title
    def getEditorial(self):
        return self.editorial
    def getCode(self):
        return self.code
    def setAuthor(self, newAuthor):
        self.author = newAuthor
    def setTitle(self, newTitle):
        self.title = newTitle        
    def setEditorial(self, newEditorial):
        self.editorial = newEditorial
    def setCode(self, newCode):
        self.code = newCode

