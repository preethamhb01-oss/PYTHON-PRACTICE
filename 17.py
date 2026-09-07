'''
Organize Code in a Package

Create a package called library with two modules:

books.py (function: list_books())
members.py (function: list_members())
Import and use both in a main file.
'''
from library import book
from library import members
book.books("Wings of fire ", "To Kill a Mockingbird", "1984", "The Great Gatsby ")

members.people("Sagar", "Arya", "Vijay")

