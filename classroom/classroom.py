# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:50:33 2026

@author: jacpe396
"""

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self, firstname, lastname, subject):
        # Use super() to call the Person constructor
        super().__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        print(f"{self.get_full_name()}, {self.subject}")


class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course

    def printNameCourse(self):
        print(f"{self.get_full_name()}, {self.course}")